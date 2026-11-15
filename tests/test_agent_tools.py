import unittest
from uuid import UUID

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.models import AgentDefinition, AgentEvent, AgentSession, User
from backend.ontology_service.app.security import Actor, create_access_token, hash_password
from backend.agent_service.app.main import create_app
from backend.agent_service.app.dependencies import get_ontology_client, get_redis


class FakeRedis:
    def __init__(self, *, fail: bool = False) -> None:
        self.values: dict[str, str] = {}
        self.lists: dict[str, list[str]] = {}
        self.expiration_seconds: dict[str, int] = {}
        self.fail = fail

    def _check(self) -> None:
        if self.fail:
            raise ConnectionError("Redis unavailable")

    def ping(self) -> bool:
        self._check()
        return True

    def set(self, key: str, value: str, ex: int | None = None) -> bool:
        self._check()
        self.values[key] = value
        return True

    def rpush(self, key: str, value: str) -> int:
        self._check()
        self.lists.setdefault(key, []).append(value)
        return len(self.lists[key])

    def lrange(self, key: str, start: int, end: int) -> list[str]:
        self._check()
        values = self.lists.get(key, [])
        return values[start:] if end == -1 else values[start : end + 1]

    def expire(self, key: str, seconds: int) -> bool:
        self._check()
        self.expiration_seconds[key] = seconds
        return True


class FakeOntologyClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, dict]] = []

    def search_objects(self, token: str, arguments: dict) -> dict:
        self.calls.append((token, "search_objects", arguments))
        return {"items": [], "total": 0}

    def get_object(self, token: str, object_id: str) -> dict:
        self.calls.append((token, "get_object", {"object_id": object_id}))
        return {"id": object_id}

    def execute_action(self, token: str, action_api_name: str, arguments: dict) -> dict:
        self.calls.append((token, "execute_action", {"action_api_name": action_api_name, **arguments}))
        return {"version": arguments["expected_version"] + 1}


class AgentToolsApiTests(unittest.TestCase):
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
        self.viewer = User(email="viewer@example.com", password_hash=hash_password("viewer-pass"), role="viewer")
        with self.session_factory() as session:
            session.add_all([self.admin, self.editor, self.viewer])
            session.commit()

        self.redis = FakeRedis()
        self.ontology_client = FakeOntologyClient()
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

    def create_agent(self, *, allowed_tools: list[str], allowed_actions: list[str] | None = None) -> UUID:
        response = self.client.post(
            "/api/agents",
            headers=self.headers_for(self.admin),
            json={
                "api_name": "operations_assistant",
                "display_name": "运营助手",
                "description": "测试 Agent",
                "allowed_tools": allowed_tools,
                "allowed_actions": allowed_actions or [],
            },
        )
        self.assertEqual(response.status_code, 201, response.text)
        agent_id = UUID(response.json()["id"])
        publish_response = self.client.post(
            f"/api/agents/{agent_id}/publish",
            headers=self.headers_for(self.admin),
        )
        self.assertEqual(publish_response.status_code, 201, publish_response.text)
        return agent_id

    def create_session(self, agent_id: UUID, user: User) -> UUID:
        response = self.client.post(
            f"/api/agents/{agent_id}/sessions",
            headers=self.headers_for(user),
        )
        self.assertEqual(response.status_code, 201, response.text)
        return UUID(response.json()["id"])

    def test_agent_cannot_call_ungranted_tool(self) -> None:
        agent_id = self.create_agent(allowed_tools=["get_object"])
        session_id = self.create_session(agent_id, self.editor)

        response = self.client.post(
            f"/api/sessions/{session_id}/tools/search_objects",
            headers=self.headers_for(self.editor),
            json={"arguments": {"query": "客户"}},
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.ontology_client.calls, [])
        with self.session_factory() as session:
            logged_event = session.scalar(
                select(AgentEvent).where(
                    AgentEvent.session_id == session_id,
                    AgentEvent.tool_name == "search_objects",
                )
            )
            self.assertEqual(logged_event.status, "denied")

    def test_agent_action_respects_actor_role(self) -> None:
        agent_id = self.create_agent(allowed_tools=["execute_action"], allowed_actions=["set_customer_tier"])
        session_id = self.create_session(agent_id, self.viewer)

        response = self.client.post(
            f"/api/sessions/{session_id}/tools/execute_action",
            headers=self.headers_for(self.viewer),
            json={
                "arguments": {
                    "action_api_name": "set_customer_tier",
                    "object_id": "00000000-0000-0000-0000-000000000001",
                    "expected_version": 1,
                    "parameters": {"tier": "preferred"},
                }
            },
        )

        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.ontology_client.calls, [])

    def test_authorized_editor_can_execute_agent_action(self) -> None:
        agent_id = self.create_agent(allowed_tools=["execute_action"], allowed_actions=["set_customer_tier"])
        session_id = self.create_session(agent_id, self.editor)

        response = self.client.post(
            f"/api/sessions/{session_id}/tools/execute_action",
            headers=self.headers_for(self.editor),
            json={
                "arguments": {
                    "action_api_name": "set_customer_tier",
                    "object_id": "00000000-0000-0000-0000-000000000001",
                    "expected_version": 1,
                    "parameters": {"tier": "preferred"},
                }
            },
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(self.ontology_client.calls[0][1], "execute_action")

    def test_closed_agent_session_rejects_more_tool_calls(self) -> None:
        agent_id = self.create_agent(allowed_tools=["search_objects"])
        session_id = self.create_session(agent_id, self.editor)
        close_response = self.client.post(
            f"/api/sessions/{session_id}/close",
            headers=self.headers_for(self.editor),
        )

        response = self.client.post(
            f"/api/sessions/{session_id}/tools/search_objects",
            headers=self.headers_for(self.editor),
            json={"arguments": {"query": "客户"}},
        )

        self.assertEqual(close_response.status_code, 200, close_response.text)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(self.ontology_client.calls, [])

    def test_agent_tool_calls_ontology_api(self) -> None:
        agent_id = self.create_agent(allowed_tools=["search_objects"])
        session_id = self.create_session(agent_id, self.editor)

        response = self.client.post(
            f"/api/sessions/{session_id}/tools/search_objects",
            headers=self.headers_for(self.editor),
            json={"arguments": {"query": "北辰"}},
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(self.ontology_client.calls[0][1], "search_objects")
        self.assertEqual(self.ontology_client.calls[0][2]["query"], "北辰")
        with self.session_factory() as session:
            event_row = session.scalar(select(AgentEvent).where(AgentEvent.session_id == session_id))
            self.assertEqual(event_row.status, "succeeded")

    def test_session_events_are_ordered(self) -> None:
        agent_id = self.create_agent(allowed_tools=["search_objects", "get_object"])
        session_id = self.create_session(agent_id, self.editor)
        headers = self.headers_for(self.editor)

        self.client.post(
            f"/api/sessions/{session_id}/tools/search_objects",
            headers=headers,
            json={"arguments": {"query": "客户"}},
        )
        self.client.post(
            f"/api/sessions/{session_id}/tools/get_object",
            headers=headers,
            json={"arguments": {"object_id": "00000000-0000-0000-0000-000000000001"}},
        )
        response = self.client.get(f"/api/sessions/{session_id}/events", headers=headers)

        self.assertEqual(response.status_code, 200, response.text)
        events = response.json()["items"]
        self.assertEqual([item["sequence"] for item in events], [1, 2, 3])
        self.assertEqual([item["event_type"] for item in events], ["session.created", "tool.called", "tool.called"])

    def test_session_event_cache_expires_after_one_day(self) -> None:
        agent_id = self.create_agent(allowed_tools=["search_objects"])
        session_id = self.create_session(agent_id, self.editor)

        self.assertEqual(self.redis.expiration_seconds[f"agent:session:{session_id}:events"], 86400)

    def test_invalid_token_cannot_create_agent_session(self) -> None:
        agent_id = self.create_agent(allowed_tools=["search_objects"])

        response = self.client.post(f"/api/agents/{agent_id}/sessions")

        self.assertEqual(response.status_code, 401)

    def test_redis_failure_is_reported_by_readiness_check(self) -> None:
        self.app.dependency_overrides[get_redis] = lambda: FakeRedis(fail=True)

        response = self.client.get("/health/ready")

        self.assertEqual(response.status_code, 503)
        self.assertIn("Redis", response.json()["detail"])
