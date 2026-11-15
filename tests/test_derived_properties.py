import unittest

from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.main import create_app
from backend.ontology_service.app.models import (
    ActionDefinition,
    DataSourceConnection,
    DataSourceMapping,
    LinkType,
    ObjectLink,
    ObjectRecord,
    ObjectType,
    Ontology,
    Project,
    ProjectMembership,
    PropertyDefinition,
    User,
)
from backend.ontology_service.app.security import Actor, create_access_token, hash_password


class DerivedPropertyApiTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)

        @event.listens_for(self.engine, "connect")
        def enable_foreign_keys(connection, _record) -> None:
            cursor = connection.cursor()
            cursor.execute("PRAGMA foreign_keys=ON")
            cursor.close()

        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
        self.settings = Settings(jwt_secret="unit-test-secret-long-enough-for-hmac-sha256")
        self.admin = User(email="admin@example.com", password_hash=hash_password("admin-pass"), role="admin")
        self.project = Project(api_name="commerce", display_name="电商项目")
        with self.session_factory() as session:
            session.add_all([self.admin, self.project])
            session.flush()
            session.add(ProjectMembership(project_id=self.project.id, user_id=self.admin.id, role="admin"))
            self.ontology = Ontology(project_id=self.project.id, api_name="commerce", display_name="交易本体")
            customer = ObjectType(ontology=self.ontology, api_name="customer", display_name="客户")
            order = ObjectType(ontology=self.ontology, api_name="order", display_name="订单")
            line = ObjectType(ontology=self.ontology, api_name="line", display_name="订单行")
            session.add_all([self.ontology, customer, order, line])
            session.flush()
            customer_orders = LinkType(
                ontology_id=self.ontology.id,
                api_name="customer_orders",
                display_name="客户订单",
                source_type_id=customer.id,
                target_type_id=order.id,
            )
            order_lines = LinkType(
                ontology_id=self.ontology.id,
                api_name="order_lines",
                display_name="订单明细",
                source_type_id=order.id,
                target_type_id=line.id,
            )
            session.add_all([customer_orders, order_lines])
            session.add_all([
                PropertyDefinition(object_type_id=customer.id, api_name="id", display_name="客户编号", data_type="string", required=True, editable=False, unique_value=True),
                PropertyDefinition(object_type_id=order.id, api_name="id", display_name="订单编号", data_type="string", required=True, editable=False, unique_value=True),
                PropertyDefinition(object_type_id=line.id, api_name="id", display_name="明细编号", data_type="string", required=True, editable=False, unique_value=True),
                PropertyDefinition(object_type_id=line.id, api_name="amount", display_name="金额", data_type="number"),
            ])
            customer_record = ObjectRecord(object_type_id=customer.id, primary_key_value="C-1", properties={"id": "C-1", "name": "甲"})
            order_one = ObjectRecord(object_type_id=order.id, primary_key_value="O-1", properties={"id": "O-1"})
            order_two = ObjectRecord(object_type_id=order.id, primary_key_value="O-2", properties={"id": "O-2"})
            line_one = ObjectRecord(object_type_id=line.id, primary_key_value="L-1", properties={"id": "L-1", "amount": 25.0})
            line_two = ObjectRecord(object_type_id=line.id, primary_key_value="L-2", properties={"id": "L-2", "amount": 100.0})
            line_three = ObjectRecord(object_type_id=line.id, primary_key_value="L-3", properties={"id": "L-3", "amount": None})
            session.add_all([customer_record, order_one, order_two, line_one, line_two, line_three])
            session.flush()
            session.add_all([
                ObjectLink(link_type_id=customer_orders.id, source_object_id=customer_record.id, target_object_id=order_one.id),
                ObjectLink(link_type_id=customer_orders.id, source_object_id=customer_record.id, target_object_id=order_two.id),
                ObjectLink(link_type_id=order_lines.id, source_object_id=order_one.id, target_object_id=line_one.id),
                ObjectLink(link_type_id=order_lines.id, source_object_id=order_one.id, target_object_id=line_two.id),
                ObjectLink(link_type_id=order_lines.id, source_object_id=order_two.id, target_object_id=line_three.id),
            ])
            self.customer_id = customer_record.id
            self.customer_type_id = customer.id
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

    def headers(self) -> dict[str, str]:
        actor = Actor(id=str(self.admin.id), email=self.admin.email, role="admin")
        token = create_access_token(actor, self.settings)
        return {"Authorization": f"Bearer {token}", "X-Project-ID": str(self.project.id)}

    async def test_preview_aggregates_multi_hop_property_and_returns_path_trace(self) -> None:
        response = await self.client.post(
            "/api/derived-properties/preview",
            headers=self.headers(),
            json={
                "ontology_id": str(self.ontology.id),
                "object_id": str(self.customer_id),
                "definition": {
                    "object_type_api_name": "customer",
                    "api_name": "customer_total_spend",
                    "display_name": "客户累计消费",
                    "data_type": "number",
                    "path": [
                        {"link_api_name": "customer_orders", "direction": "outgoing"},
                        {"link_api_name": "order_lines", "direction": "outgoing"},
                    ],
                    "terminal_property_api_name": "amount",
                    "aggregation": "sum",
                },
            },
        )

        self.assertEqual(response.status_code, 200, response.text)
        payload = response.json()
        self.assertEqual(payload["value"], 125.0)
        self.assertEqual(payload["matched_count"], 2)
        self.assertEqual(payload["aggregation"], "sum")
        hop_trace = [step for step in payload["trace"] if "link_api_name" in step]
        self.assertEqual({step["link_api_name"] for step in hop_trace}, {"customer_orders", "order_lines"})
        self.assertTrue(all("source_object_id" in step and "target_object_id" in step for step in hop_trace))

    async def test_canvas_returns_real_types_links_actions_and_source_mappings(self) -> None:
        with self.session_factory() as session:
            source = DataSourceConnection(
                ontology_id=self.ontology.id,
                created_by_id=self.admin.id,
                name="订单仓库",
                connector_type="local_file",
                status="ready",
            )
            session.add(source)
            session.flush()
            session.add(DataSourceMapping(
                connection_id=source.id,
                object_type_id=self.customer_type_id,
                primary_key_field="customer_id",
                field_mappings={"customer_name": "name"},
            ))
            customer = session.get(ObjectType, self.customer_type_id)
            session.add(ActionDefinition(
                ontology_id=self.ontology.id,
                object_type_id=customer.id,
                api_name="refresh_customer",
                display_name="刷新客户",
                allowed_properties=["name"],
                parameters_schema={},
            ))
            session.commit()

        response = await self.client.get(
            "/api/ontology/canvas",
            headers=self.headers(),
            params={"ontology_id": str(self.ontology.id)},
        )

        self.assertEqual(response.status_code, 200, response.text)
        canvas = response.json()
        self.assertEqual({node["id"] for node in canvas["nodes"] if node["type"] == "objectType"}, {
            "object_type:customer", "object_type:order", "object_type:line",
        })
        self.assertIn("link:customer_orders", {edge["id"] for edge in canvas["edges"]})
        self.assertIn("link:order_lines", {edge["id"] for edge in canvas["edges"]})
        self.assertIn("action:refresh_customer", {node["id"] for node in canvas["nodes"]})
        self.assertTrue(any(edge["type"] == "sourceMapping" for edge in canvas["edges"]))


if __name__ == "__main__":
    unittest.main()
