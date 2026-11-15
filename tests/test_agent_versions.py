import unittest
from uuid import UUID

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.agent_service.app.dependencies import get_ontology_client, get_redis
from backend.agent_service.app.main import create_app
from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.models import AgentEvent, AgentSession, User
from backend.ontology_service.app.security import Actor, create_access_token, hash_password


class FakeRedis:
    def __init__(self) -> None:
        self.values: dict[str, str] = {}
        self.lists: dict[str, list[str]] = {}

    def set(self, key: str, value: str, ex: int | None = None) -> bool:
        self.values[key] = value
        return True

    def rpush(self, key: str, value: str) -> int:
        self.lists.setdefault(key, []).append(value)
        return len(self.lists[key])

    def lrange(self, key: str, start: int, end: int) -> list[str]:
        values = self.lists.get(key, [])
        return values[start:] if end == -1 else values[start : end + 1]

    def expire(self, _key: str, _seconds: int) -> bool:
        return True


class FakeOntologyClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict]] = []

    def search_objects(self, _token: str, arguments: dict) -> dict:
        self.calls.append(("search_objects", arguments))
        return {"items": [], "total": 0}


class FakeModelProvider:
    def __init__(self, responses: list[dict]) -> None:
        self.responses = list(responses)
        self.calls: list[dict] = []

    def complete(self, *, model: str, messages: list[dict], tools: list[dict]) -> dict:
        self.calls.append({"model": model, "messages": messages, "tools": tools})
        return self.responses.pop(0)


class AgentVersionApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )

        @event.listens_for(self.engine, "connect")
        def enable_foreign_keys(connection, _record) -> None:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
        self.settings = Settings(jwt_secret="unit-test-secret-long-enough-for-hmac-sha256")
        self.admin = User(email="admin@example.com", password_hash=hash_password("admin-pass"), role="admin")
        self.editor = User(email="editor@example.com", password_hash=hash_password("editor-pass"), role="editor")
        with self.session_factory() as session:
            session.add_all([self.admin, self.editor])
            session.commit()

        self.redis = FakeRedis()
        self.ontology_client = FakeOntologyClient()
        self.model_provider = None
        self.app = create_app(self.settings)

        def override_get_db():
            with self.session_factory() as session:
                yield session

        self.app.dependency_overrides[get_db] = override_get_db
        self.app.dependency_overrides[get_redis] = lambda: self.redis
        self.app.dependency_overrides[get_ontology_client] = lambda: self.ontology_client
        self.client = TestClient(self.app)

    def tearDown(self) -> None:
        self.client.close()
        self.engine.dispose()

    def headers_for(self, user: User) -> dict[str, str]:
        actor = Actor(id=str(user.id), email=user.email, role=user.role)
        token = create_access_token(actor, self.settings)
        return {"Authorization": f"Bearer {token}"}

    def create_agent(self) -> UUID:
        response = self.client.post(
            "/api/agents",
            headers=self.headers_for(self.admin),
            json={
                "api_name": "operations_assistant",
                "display_name": "运营助理",
                "description": "客户运营 Agent",
                "allowed_tools": ["search_objects"],
                "allowed_actions": [],
                "draft_config": {
                    "model_provider": "local",
                    "model_name": "确定性本地预览",
                    "system_prompt": "根据运营知识图谱协助处理客户问题。",
                    "initial_user_message": "请检查客户 {{customer_id}}。",
                    "inputs": [
                        {
                            "name": "customer_id",
                            "display_name": "客户编号",
                            "type": "string",
                            "required": True,
                        }
                    ],
                    "precomputed_variables": [
                        {"name": "customer_context", "expression": "input.customer_id"}
                    ],
                    "allowed_tools": ["search_objects"],
                    "allowed_actions": [],
                    "session_completion": {"mode": "stays_open", "output_schema": {}},
                },
            },
        )
        self.assertEqual(response.status_code, 201, response.text)
        return UUID(response.json()["id"])

    def test_published_agent_version_is_immutable(self) -> None:
        agent_id = self.create_agent()
        headers = self.headers_for(self.admin)
        first_publish = self.client.post(f"/api/agents/{agent_id}/publish", headers=headers)
        self.assertEqual(first_publish.status_code, 201, first_publish.text)
        self.assertEqual(first_publish.json()["version_number"], 1)
        original_prompt = first_publish.json()["config"]["system_prompt"]

        updated_config = first_publish.json()["config"] | {"system_prompt": "新版提示词"}
        updated_config.pop("id", None)
        updated_config.pop("version_number", None)
        update = self.client.put(
            f"/api/agents/{agent_id}",
            headers=headers,
            json={"draft_config": updated_config},
        )
        versions = self.client.get(f"/api/agents/{agent_id}/versions", headers=headers)

        self.assertEqual(update.status_code, 200, update.text)
        self.assertEqual(versions.status_code, 200, versions.text)
        self.assertEqual(versions.json()[0]["config"]["system_prompt"], original_prompt)
        self.assertEqual(versions.json()[0]["version_number"], 1)

    def test_new_session_requires_inputs_and_pins_published_version(self) -> None:
        agent_id = self.create_agent()
        headers = self.headers_for(self.editor)
        missing = self.client.post(f"/api/agents/{agent_id}/sessions", headers=headers, json={"inputs": {}})
        self.assertEqual(missing.status_code, 409)

        publish = self.client.post(f"/api/agents/{agent_id}/publish", headers=self.headers_for(self.admin))
        self.assertEqual(publish.status_code, 201, publish.text)
        missing = self.client.post(f"/api/agents/{agent_id}/sessions", headers=headers, json={"inputs": {}})
        valid = self.client.post(
            f"/api/agents/{agent_id}/sessions",
            headers=headers,
            json={"inputs": {"customer_id": "C-100"}},
        )

        self.assertEqual(missing.status_code, 422)
        self.assertEqual(valid.status_code, 201, valid.text)
        self.assertEqual(valid.json()["version_number"], 1)
        self.assertEqual(valid.json()["inputs"], {"customer_id": "C-100"})

    def test_preview_validates_inputs_without_creating_session_or_calling_tools(self) -> None:
        agent_id = self.create_agent()

        response = self.client.post(
            f"/api/agents/{agent_id}/preview",
            headers=self.headers_for(self.admin),
            json={"inputs": {"customer_id": "C-100"}},
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["mode"], "deterministic_dry_run")
        self.assertIn("C-100", response.json()["rendered_prompt"])
        self.assertEqual(self.ontology_client.calls, [])
        with self.session_factory() as session:
            self.assertEqual(session.scalar(select(AgentSession.id)), None)
            self.assertEqual(session.scalar(select(AgentEvent.id)), None)

    def test_running_session_keeps_tool_scope_from_its_pinned_version(self) -> None:
        agent_id = self.create_agent()
        admin_headers = self.headers_for(self.admin)
        first = self.client.post(f"/api/agents/{agent_id}/publish", headers=admin_headers)
        session_response = self.client.post(
            f"/api/agents/{agent_id}/sessions",
            headers=self.headers_for(self.editor),
            json={"inputs": {"customer_id": "C-100"}},
        )
        agent_response = self.client.get(f"/api/agents/{agent_id}", headers=admin_headers)
        second_config = agent_response.json()["draft_config"]
        second_config["allowed_tools"] = ["get_object"]
        update = self.client.put(
            f"/api/agents/{agent_id}",
            headers=admin_headers,
            json={"draft_config": second_config},
        )
        second = self.client.post(f"/api/agents/{agent_id}/publish", headers=admin_headers)
        call = self.client.post(
            f"/api/sessions/{session_response.json()['id']}/tools/search_objects",
            headers=self.headers_for(self.editor),
            json={"arguments": {"query": "北辰"}},
        )

        self.assertEqual(first.status_code, 201, first.text)
        self.assertEqual(session_response.status_code, 201, session_response.text)
        self.assertEqual(update.status_code, 200, update.text)
        self.assertEqual(second.status_code, 201, second.text)
        self.assertEqual(call.status_code, 200, call.text)

    def test_agent_manager_filters_by_origin_and_opens_pinned_session_details(self) -> None:
        agent_id = self.create_agent()
        self.client.post(f"/api/agents/{agent_id}/publish", headers=self.headers_for(self.admin))
        headers = self.headers_for(self.editor)
        workshop_session = self.client.post(
            f"/api/agents/{agent_id}/sessions",
            headers=headers,
            json={"inputs": {"customer_id": "C-100"}, "origin_resource": "Workshop"},
        )
        automate_session = self.client.post(
            f"/api/agents/{agent_id}/sessions",
            headers=headers,
            json={"inputs": {"customer_id": "C-200"}, "origin_resource": "Automate"},
        )

        filtered = self.client.get(
            "/api/sessions?origin_resource=Workshop&status=active",
            headers=headers,
        )
        detail = self.client.get(f"/api/sessions/{workshop_session.json()['id']}", headers=headers)

        self.assertEqual(workshop_session.status_code, 201, workshop_session.text)
        self.assertEqual(automate_session.status_code, 201, automate_session.text)
        self.assertEqual(filtered.status_code, 200, filtered.text)
        self.assertEqual(filtered.json()["total"], 1)
        self.assertEqual(filtered.json()["items"][0]["origin_resource"], "Workshop")
        self.assertEqual(detail.status_code, 200, detail.text)
        self.assertEqual(detail.json()["version_number"], 1)
        self.assertEqual(detail.json()["events"][0]["event_type"], "session.created")

    def test_agent_runtime_lists_environment_backed_providers_without_secrets(self) -> None:
        response = self.client.get("/api/agent-runtime/capabilities", headers=self.headers_for(self.admin))

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["providers"][0]["id"], "local")
        self.assertFalse(response.json()["providers"][1]["available"])
        self.assertNotIn("api_key", response.text.lower())

    def test_agent_message_requires_configured_model_runtime(self) -> None:
        agent_id = self.create_agent()
        headers = self.headers_for(self.admin)
        current = self.client.get(f"/api/agents/{agent_id}", headers=headers).json()
        config = current["draft_config"]
        config["model_provider"] = "openai-compatible"
        updated = self.client.put(
            f"/api/agents/{agent_id}", headers=headers, json={"draft_config": config}
        )
        published = self.client.post(f"/api/agents/{agent_id}/publish", headers=headers)
        session_response = self.client.post(
            f"/api/agents/{agent_id}/sessions",
            headers=self.headers_for(self.editor),
            json={"inputs": {"customer_id": "C-100"}},
        )

        response = self.client.post(
            f"/api/sessions/{session_response.json()['id']}/messages",
            headers=self.headers_for(self.editor),
            json={"content": "查找这个客户"},
        )

        self.assertEqual(updated.status_code, 200, updated.text)
        self.assertEqual(published.status_code, 201, published.text)
        self.assertEqual(session_response.status_code, 201, session_response.text)
        self.assertEqual(response.status_code, 409)
        self.assertIn("模型运行时", response.json()["detail"])

    def test_agent_message_runs_only_pinned_tools_and_records_the_turn(self) -> None:
        agent_id = self.create_agent()
        admin_headers = self.headers_for(self.admin)
        current = self.client.get(f"/api/agents/{agent_id}", headers=admin_headers).json()
        config = current["draft_config"]
        config["model_provider"] = "openai-compatible"
        update = self.client.put(
            f"/api/agents/{agent_id}", headers=admin_headers, json={"draft_config": config}
        )
        publish = self.client.post(f"/api/agents/{agent_id}/publish", headers=admin_headers)
        session_response = self.client.post(
            f"/api/agents/{agent_id}/sessions",
            headers=self.headers_for(self.editor),
            json={"inputs": {"customer_id": "C-100"}},
        )
        self.model_provider = FakeModelProvider([
            {
                "request_id": "trace-1",
                "message": {
                    "content": None,
                    "tool_calls": [{
                        "id": "call-1",
                        "type": "function",
                        "function": {"name": "search_objects", "arguments": "{\"query\":\"C-100\"}"},
                    }],
                },
                "usage": {"prompt_tokens": 10, "completion_tokens": 2},
            },
            {
                "request_id": "trace-2",
                "message": {"content": "已查询客户 C-100。", "tool_calls": []},
                "usage": {"prompt_tokens": 18, "completion_tokens": 6},
            },
        ])
        self.app.state.agent_model_provider = self.model_provider

        response = self.client.post(
            f"/api/sessions/{session_response.json()['id']}/messages",
            headers=self.headers_for(self.editor),
            json={"content": "查找客户 C-100"},
        )
        events = self.client.get(
            f"/api/sessions/{session_response.json()['id']}/events",
            headers=self.headers_for(self.editor),
        )

        self.assertEqual(update.status_code, 200, update.text)
        self.assertEqual(publish.status_code, 201, publish.text)
        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["assistant_message"], "已查询客户 C-100。")
        self.assertEqual([call["model"] for call in self.model_provider.calls], ["确定性本地预览", "确定性本地预览"])
        self.assertEqual([tool["function"]["name"] for tool in self.model_provider.calls[0]["tools"]], ["search_objects"])
        first_turn_user_messages = [message for message in self.model_provider.calls[0]["messages"] if message["role"] == "user"]
        self.assertEqual([message["content"] for message in first_turn_user_messages], ["请检查客户 C-100。", "查找客户 C-100"])
        self.assertEqual(self.ontology_client.calls[0][0], "search_objects")
        event_types = [item["event_type"] for item in events.json()["items"]]
        self.assertLess(event_types.index("message.user"), event_types.index("tool.called"))
        self.assertLess(event_types.index("tool.called"), event_types.index("message.assistant"))
