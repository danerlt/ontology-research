import unittest
from uuid import UUID

from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine, event, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.main import create_app
from backend.ontology_service.app.models import (
    ActionDefinition,
    AuditEvent,
    LinkType,
    ObjectLink,
    ObjectRecord,
    ObjectType,
    Ontology,
    PropertyDefinition,
    User,
)
from backend.ontology_service.app.security import Actor, create_access_token, hash_password


class ObjectsAndActionsApiTests(unittest.IsolatedAsyncioTestCase):
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
        self.ontology = Ontology(api_name="operations", display_name="运营本体", revision=1)
        with self.session_factory() as session:
            session.add_all([self.admin, self.editor, self.viewer, self.ontology])
            session.flush()
            self.customer_type = ObjectType(
                ontology_id=self.ontology.id,
                api_name="customer",
                display_name="客户",
                primary_key_property="id",
            )
            self.order_type = ObjectType(
                ontology_id=self.ontology.id,
                api_name="order",
                display_name="订单",
                primary_key_property="id",
            )
            session.add_all([self.customer_type, self.order_type])
            session.flush()
            session.add_all(
                [
                    PropertyDefinition(
                        object_type_id=self.customer_type.id,
                        api_name="id",
                        display_name="客户编号",
                        data_type="string",
                        required=True,
                        editable=False,
                        unique_value=True,
                    ),
                    PropertyDefinition(
                        object_type_id=self.customer_type.id,
                        api_name="name",
                        display_name="名称",
                        data_type="string",
                        required=True,
                    ),
                    PropertyDefinition(
                        object_type_id=self.customer_type.id,
                        api_name="tier",
                        display_name="等级",
                        data_type="enum",
                        options={"choices": ["standard", "preferred"]},
                    ),
                    PropertyDefinition(
                        object_type_id=self.order_type.id,
                        api_name="id",
                        display_name="订单编号",
                        data_type="string",
                        required=True,
                        editable=False,
                        unique_value=True,
                    ),
                    PropertyDefinition(
                        object_type_id=self.order_type.id,
                        api_name="amount",
                        display_name="金额",
                        data_type="number",
                        required=True,
                    ),
                ]
            )
            self.customer = ObjectRecord(
                object_type_id=self.customer_type.id,
                primary_key_value="C-100",
                properties={"id": "C-100", "name": "北辰制造", "tier": "standard"},
            )
            self.order = ObjectRecord(
                object_type_id=self.order_type.id,
                primary_key_value="O-100",
                properties={"id": "O-100", "amount": 1200.0},
            )
            self.customer_order_link = LinkType(
                ontology_id=self.ontology.id,
                api_name="customer_orders",
                display_name="客户订单",
                source_type_id=self.customer_type.id,
                target_type_id=self.order_type.id,
            )
            self.action = ActionDefinition(
                ontology_id=self.ontology.id,
                object_type_id=self.customer_type.id,
                api_name="set_customer_tier",
                display_name="设置客户等级",
                allowed_properties=["tier"],
                parameters_schema={"tier": {"required": True}},
            )
            session.add_all([self.customer, self.order, self.customer_order_link, self.action])
            session.flush()
            session.add(
                ObjectLink(
                    link_type_id=self.customer_order_link.id,
                    source_object_id=self.customer.id,
                    target_object_id=self.order.id,
                )
            )
            session.commit()
        self.app = create_app(self.settings)

        def override_get_db():
            with self.session_factory() as session:
                yield session

        self.app.dependency_overrides[get_db] = override_get_db
        self.client = AsyncClient(transport=ASGITransport(app=self.app), base_url="http://test")

    async def asyncTearDown(self) -> None:
        await self.client.aclose()
        self.engine.dispose()

    def headers_for(self, user: User) -> dict[str, str]:
        actor = Actor(id=str(user.id), email=user.email, role=user.role)
        token = create_access_token(actor, self.settings)
        return {"Authorization": f"Bearer {token}"}

    async def test_objects_are_validated_against_type(self) -> None:
        response = await self.client.post(
            "/api/objects",
            headers=self.headers_for(self.editor),
            json={
                "ontology_id": str(self.ontology.id),
                "object_type_api_name": "customer",
                "primary_key_value": "C-200",
                "properties": {"name": 42},
            },
        )

        self.assertEqual(response.status_code, 422)

    async def test_datetime_property_rejects_non_string_values(self) -> None:
        with self.session_factory() as session:
            session.add(
                PropertyDefinition(
                    object_type_id=self.customer_type.id,
                    api_name="last_seen",
                    display_name="最近活跃时间",
                    data_type="datetime",
                )
            )
            session.commit()

        response = await self.client.post(
            "/api/objects",
            headers=self.headers_for(self.editor),
            json={
                "ontology_id": str(self.ontology.id),
                "object_type_api_name": "customer",
                "primary_key_value": "C-201",
                "properties": {"name": "新客户", "last_seen": 123},
            },
        )

        self.assertEqual(response.status_code, 422)

    async def test_object_creation_requires_required_properties(self) -> None:
        response = await self.client.post(
            "/api/objects",
            headers=self.headers_for(self.editor),
            json={
                "ontology_id": str(self.ontology.id),
                "object_type_api_name": "customer",
                "primary_key_value": "C-200",
                "properties": {},
            },
        )

        self.assertEqual(response.status_code, 422)

    async def test_object_search_is_paginated(self) -> None:
        for key, name in (("C-200", "北辰分部"), ("C-300", "南辰公司")):
            response = await self.client.post(
                "/api/objects",
                headers=self.headers_for(self.editor),
                json={
                    "ontology_id": str(self.ontology.id),
                    "object_type_api_name": "customer",
                    "primary_key_value": key,
                    "properties": {"name": name},
                },
            )
            self.assertEqual(response.status_code, 201, response.text)

        response = await self.client.get(
            "/api/objects",
            headers=self.headers_for(self.viewer),
            params={"object_type_api_name": "customer", "query": "北辰", "page": 1, "page_size": 1},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["total"], 2)
        self.assertEqual(len(response.json()["items"]), 1)

    async def test_object_list_sorts_by_allowlisted_server_fields(self) -> None:
        for key, name in (("C-200", "北辰分部"), ("C-300", "南辰公司")):
            created = await self.client.post(
                "/api/objects",
                headers=self.headers_for(self.editor),
                json={
                    "ontology_id": str(self.ontology.id),
                    "object_type_api_name": "customer",
                    "primary_key_value": key,
                    "properties": {"name": name},
                },
            )
            self.assertEqual(created.status_code, 201, created.text)

        response = await self.client.get(
            "/api/objects",
            headers=self.headers_for(self.viewer),
            params={"object_type_api_name": "customer", "sort_by": "primary_key", "sort_order": "asc"},
        )
        descending = await self.client.get(
            "/api/objects",
            headers=self.headers_for(self.viewer),
            params={"object_type_api_name": "customer", "sort_by": "primary_key", "sort_order": "desc"},
        )
        invalid_sort = await self.client.get(
            "/api/objects",
            headers=self.headers_for(self.viewer),
            params={"object_type_api_name": "customer", "sort_by": "properties"},
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual([item["primary_key_value"] for item in response.json()["items"]], ["C-100", "C-200", "C-300"])
        self.assertEqual([item["primary_key_value"] for item in descending.json()["items"]], ["C-300", "C-200", "C-100"])
        self.assertEqual(invalid_sort.status_code, 422)

    async def test_object_detail_contains_links(self) -> None:
        response = await self.client.get(
            f"/api/objects/{self.customer.id}",
            headers=self.headers_for(self.viewer),
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["links"][0]["link_type_api_name"], "customer_orders")
        self.assertEqual(response.json()["links"][0]["target_object_id"], str(self.order.id))

    async def test_editor_can_create_directional_object_link(self) -> None:
        create_target = await self.client.post(
            "/api/objects",
            headers=self.headers_for(self.editor),
            json={
                "ontology_id": str(self.ontology.id),
                "object_type_api_name": "order",
                "primary_key_value": "O-200",
                "properties": {"amount": 450.0},
            },
        )
        target_id = create_target.json()["id"]

        response = await self.client.post(
            f"/api/objects/{self.customer.id}/links",
            headers=self.headers_for(self.editor),
            json={"link_type_api_name": "customer_orders", "target_object_id": target_id},
        )

        self.assertEqual(response.status_code, 201, response.text)
        self.assertEqual(response.json()["direction"], "outgoing")
        self.assertEqual(response.json()["linked_primary_key"], "O-200")

    async def test_object_link_rejects_wrong_direction(self) -> None:
        response = await self.client.post(
            f"/api/objects/{self.order.id}/links",
            headers=self.headers_for(self.editor),
            json={"link_type_api_name": "customer_orders", "target_object_id": str(self.customer.id)},
        )

        self.assertEqual(response.status_code, 422)

    async def test_action_definitions_are_listed_for_the_object_type(self) -> None:
        response = await self.client.get(
            "/api/actions",
            headers=self.headers_for(self.viewer),
            params={"ontology_id": str(self.ontology.id), "object_type_api_name": "customer"},
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()[0]["api_name"], "set_customer_tier")

    async def test_viewer_does_not_see_sensitive_object_properties(self) -> None:
        with self.session_factory() as session:
            record = session.get(ObjectRecord, self.customer.id)
            record.properties = {**record.properties, "tax_id": "TX-001"}
            session.add(
                PropertyDefinition(
                    object_type_id=self.customer_type.id,
                    api_name="tax_id",
                    display_name="税号",
                    data_type="string",
                    sensitive=True,
                )
            )
            session.commit()

        viewer_response = await self.client.get(
            f"/api/objects/{self.customer.id}",
            headers=self.headers_for(self.viewer),
        )
        editor_response = await self.client.get(
            f"/api/objects/{self.customer.id}",
            headers=self.headers_for(self.editor),
        )

        self.assertNotIn("tax_id", viewer_response.json()["properties"])
        self.assertEqual(editor_response.json()["properties"]["tax_id"], "TX-001")

        list_response = await self.client.get(
            "/api/objects",
            headers=self.headers_for(self.viewer),
            params={"object_type_api_name": "customer"},
        )

        self.assertEqual(list_response.status_code, 200, list_response.text)
        self.assertNotIn("tax_id", list_response.json()["items"][0]["properties"])

    async def test_sensitive_action_values_are_redacted_in_audit(self) -> None:
        with self.session_factory() as session:
            record = session.get(ObjectRecord, self.customer.id)
            record.properties = {**record.properties, "tax_id": "TX-001"}
            session.add(
                PropertyDefinition(
                    object_type_id=self.customer_type.id,
                    api_name="tax_id",
                    display_name="税号",
                    data_type="string",
                    sensitive=True,
                )
            )
            session.add(
                ActionDefinition(
                    ontology_id=self.ontology.id,
                    object_type_id=self.customer_type.id,
                    api_name="update_tax_id",
                    display_name="更新税号",
                    allowed_properties=["tax_id"],
                    parameters_schema={"tax_id": {"required": True}},
                )
            )
            session.commit()

        response = await self.client.post(
            "/api/actions/update_tax_id/execute",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tax_id": "TX-002"},
            },
        )

        self.assertEqual(response.status_code, 200, response.text)
        with self.session_factory() as session:
            audit = session.scalar(select(AuditEvent).where(AuditEvent.event_type == "action.executed"))
        self.assertEqual(audit.details["changes"]["tax_id"], {"redacted": True})

    async def test_action_updates_allowlisted_properties_and_writes_audit(self) -> None:
        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/execute",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tier": "preferred"},
            },
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["properties"]["tier"], "preferred")
        self.assertEqual(response.json()["version"], 2)
        with self.session_factory() as session:
            audit = session.scalar(select(AuditEvent).where(AuditEvent.event_type == "action.executed"))
        self.assertEqual(audit.details["changes"]["tier"]["before"], "standard")

    async def test_action_rejects_properties_outside_allowlist(self) -> None:
        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/execute",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"name": "篡改名称"},
            },
        )

        self.assertEqual(response.status_code, 422)
        with self.session_factory() as session:
            record = session.get(ObjectRecord, self.customer.id)
        self.assertEqual(record.properties["name"], "北辰制造")

    async def test_failed_action_does_not_partially_write(self) -> None:
        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/execute",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tier": "preferred", "name": "篡改名称"},
            },
        )

        self.assertEqual(response.status_code, 422)
        with self.session_factory() as session:
            record = session.get(ObjectRecord, self.customer.id)
        self.assertEqual(record.properties["tier"], "standard")
        self.assertEqual(record.version, 1)

    async def test_viewer_cannot_execute_action(self) -> None:
        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/execute",
            headers=self.headers_for(self.viewer),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tier": "preferred"},
            },
        )

        self.assertEqual(response.status_code, 403)

    async def test_action_requires_its_required_parameters(self) -> None:
        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/execute",
            headers=self.headers_for(self.editor),
            json={"object_id": str(self.customer.id), "expected_version": 1, "parameters": {}},
        )

        self.assertEqual(response.status_code, 422)

    async def test_action_parameters_must_match_declared_schema(self) -> None:
        with self.session_factory() as session:
            action = session.get(ActionDefinition, self.action.id)
            action.parameters_schema = {
                "tier": {"required": True, "type": "string", "enum": ["standard"]}
            }
            session.commit()

        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/execute",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tier": "preferred"},
            },
        )

        self.assertEqual(response.status_code, 422)
        with self.session_factory() as session:
            record = session.get(ObjectRecord, self.customer.id)
        self.assertEqual(record.properties["tier"], "standard")
        self.assertEqual(record.version, 1)

    async def test_action_preview_does_not_write_record_or_audit(self) -> None:
        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/preview",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tier": "preferred"},
            },
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["property_changes"][0]["after"], "preferred")
        with self.session_factory() as session:
            record = session.get(ObjectRecord, self.customer.id)
            audit = session.scalar(select(AuditEvent).where(AuditEvent.event_type == "action.executed"))
        self.assertEqual(record.properties["tier"], "standard")
        self.assertEqual(record.version, 1)
        self.assertIsNone(audit)

    async def test_submission_criteria_blocks_invalid_object_state(self) -> None:
        with self.session_factory() as session:
            action = session.get(ActionDefinition, self.action.id)
            action.submission_criteria = {
                "all": [{"property": "tier", "operator": "equals", "value": "preferred"}]
            }
            session.commit()

        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/execute",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tier": "preferred"},
            },
        )

        self.assertEqual(response.status_code, 409)
        with self.session_factory() as session:
            record = session.get(ObjectRecord, self.customer.id)
        self.assertEqual(record.properties["tier"], "standard")
        self.assertEqual(record.version, 1)

    async def test_action_rejects_submission_criteria_with_unknown_property(self) -> None:
        with self.session_factory() as session:
            action = session.get(ActionDefinition, self.action.id)
            action.submission_criteria = {
                "property": "missing_property",
                "operator": "equals",
                "value": None,
            }
            session.commit()

        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/preview",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tier": "preferred"},
            },
        )

        self.assertEqual(response.status_code, 422)
        self.assertIn("未定义", response.json()["detail"])

    async def test_action_rejects_excessively_nested_submission_criteria(self) -> None:
        criteria: dict = {"property": "tier", "operator": "equals", "value": "standard"}
        for _ in range(24):
            criteria = {"not": criteria}
        with self.session_factory() as session:
            action = session.get(ActionDefinition, self.action.id)
            action.submission_criteria = criteria
            session.commit()

        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/preview",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 1,
                "parameters": {"tier": "preferred"},
            },
        )

        self.assertEqual(response.status_code, 422)
        self.assertIn("嵌套", response.json()["detail"])

    async def test_action_rejects_stale_object_version(self) -> None:
        response = await self.client.post(
            f"/api/actions/{self.action.api_name}/execute",
            headers=self.headers_for(self.editor),
            json={
                "object_id": str(self.customer.id),
                "expected_version": 0,
                "parameters": {"tier": "preferred"},
            },
        )

        self.assertEqual(response.status_code, 409)
        with self.session_factory() as session:
            record = session.get(ObjectRecord, self.customer.id)
        self.assertEqual(record.properties["tier"], "standard")

    async def test_unique_primary_key_is_enforced(self) -> None:
        response = await self.client.post(
            "/api/objects",
            headers=self.headers_for(self.editor),
            json={
                "ontology_id": str(self.ontology.id),
                "object_type_api_name": "customer",
                "primary_key_value": "C-100",
                "properties": {"name": "重复客户"},
            },
        )

        self.assertEqual(response.status_code, 409)

    async def test_audit_events_are_visible_to_viewers(self) -> None:
        response = await self.client.get("/api/audit-events", headers=self.headers_for(self.viewer))

        self.assertEqual(response.status_code, 200)
        self.assertIn("data", response.json())


if __name__ == "__main__":
    unittest.main()
