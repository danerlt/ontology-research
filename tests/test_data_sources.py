import unittest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine, event, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.main import create_app
from backend.ontology_service.app.models import AuditEvent, ObjectRecord, ObjectType, Ontology, Project, ProjectMembership, PropertyDefinition, User
from backend.ontology_service.app.security import Actor, create_access_token, hash_password


class DataSourceApiTests(unittest.IsolatedAsyncioTestCase):
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
        self.project = Project(api_name="test_project", display_name="测试项目")
        with self.session_factory() as session:
            session.add_all([self.admin, self.editor, self.viewer, self.project])
            session.flush()
            self.ontology = Ontology(project_id=self.project.id, api_name="operations", display_name="运营本体")
            session.add_all([
                self.ontology,
                ProjectMembership(project_id=self.project.id, user_id=self.admin.id, role="admin"),
                ProjectMembership(project_id=self.project.id, user_id=self.editor.id, role="editor"),
                ProjectMembership(project_id=self.project.id, user_id=self.viewer.id, role="viewer"),
            ])
            session.flush()
            self.customer_type = ObjectType(
                ontology_id=self.ontology.id,
                api_name="customer",
                display_name="客户",
                primary_key_property="id",
            )
            session.add(self.customer_type)
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
                        display_name="客户名称",
                        data_type="string",
                        required=True,
                    ),
                    PropertyDefinition(
                        object_type_id=self.customer_type.id,
                        api_name="tier",
                        display_name="客户等级",
                        data_type="enum",
                        options={"choices": ["standard", "preferred"]},
                    ),
                    PropertyDefinition(
                        object_type_id=self.customer_type.id,
                        api_name="credit_limit",
                        display_name="授信额度",
                        data_type="number",
                    ),
                ]
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

    async def create_source_and_mapping(self, *, field_mappings: dict | None = None) -> tuple[str, str]:
        source = await self.client.post(
            "/api/data-sources",
            headers=self.headers_for(self.editor),
            json={"ontology_id": str(self.ontology.id), "name": "客户 CSV", "description": "本地演示文件"},
        )
        self.assertEqual(source.status_code, 201, source.text)
        source_id = source.json()["id"]
        mapping = await self.client.put(
            f"/api/data-sources/{source_id}/mappings",
            headers=self.headers_for(self.editor),
            json={
                "object_type_api_name": "customer",
                "primary_key_field": "customer_id",
                "field_mappings": field_mappings or {"customer_id": "id", "full_name": "name", "segment": "tier"},
            },
        )
        self.assertEqual(mapping.status_code, 200, mapping.text)
        return source_id, mapping.json()["id"]

    async def test_preview_validates_mappings_without_writing_objects_or_audit(self) -> None:
        source_id, mapping_id = await self.create_source_and_mapping()
        response = await self.client.post(
            f"/api/data-sources/{source_id}/mappings/{mapping_id}/preview",
            headers=self.headers_for(self.editor),
            json={"rows": [{"customer_id": "C-100", "full_name": "北辰制造", "segment": "preferred"}]},
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertTrue(response.json()["valid"])
        self.assertEqual(response.json()["items"][0]["properties"]["name"], "北辰制造")
        with self.session_factory() as session:
            self.assertEqual(session.scalars(select(ObjectRecord)).all(), [])
            import_events = session.scalars(
                select(AuditEvent).where(AuditEvent.event_type.like("datasource.import.%"))
            ).all()
        self.assertEqual(import_events, [])

    async def test_import_persists_all_rows_and_records_sync_audit(self) -> None:
        source_id, mapping_id = await self.create_source_and_mapping()
        response = await self.client.post(
            f"/api/data-sources/{source_id}/mappings/{mapping_id}/import",
            headers=self.headers_for(self.editor),
            json={"rows": [
                {"customer_id": "C-100", "full_name": "北辰制造", "segment": "preferred"},
                {"customer_id": "C-200", "full_name": "南辰物流", "segment": "standard"},
            ]},
        )

        self.assertEqual(response.status_code, 201, response.text)
        self.assertEqual(response.json()["status"], "completed")
        self.assertEqual(response.json()["rows_imported"], 2)
        with self.session_factory() as session:
            records = session.scalars(select(ObjectRecord).order_by(ObjectRecord.primary_key_value)).all()
            audit = session.scalar(select(AuditEvent).where(AuditEvent.event_type == "datasource.import.completed"))
        self.assertEqual([record.primary_key_value for record in records], ["C-100", "C-200"])
        self.assertIsNotNone(audit)
        self.assertEqual(audit.details["rows_imported"], 2)

    async def test_csv_numeric_values_are_converted_using_the_target_property_type(self) -> None:
        source_id, mapping_id = await self.create_source_and_mapping(
            field_mappings={"customer_id": "id", "full_name": "name", "limit": "credit_limit"}
        )
        response = await self.client.post(
            f"/api/data-sources/{source_id}/mappings/{mapping_id}/preview",
            headers=self.headers_for(self.editor),
            json={"rows": [{"customer_id": "C-400", "full_name": "北辰制造", "limit": "12500.5"}]},
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertTrue(response.json()["valid"], response.text)
        self.assertEqual(response.json()["items"][0]["properties"]["credit_limit"], 12500.5)

    async def test_duplicate_primary_keys_fail_import_without_partial_writes(self) -> None:
        source_id, mapping_id = await self.create_source_and_mapping()
        response = await self.client.post(
            f"/api/data-sources/{source_id}/mappings/{mapping_id}/import",
            headers=self.headers_for(self.editor),
            json={"rows": [
                {"customer_id": "C-100", "full_name": "北辰制造", "segment": "standard"},
                {"customer_id": "C-100", "full_name": "重复客户", "segment": "preferred"},
            ]},
        )

        self.assertEqual(response.status_code, 422)
        issues = response.json()["detail"]["errors"]
        self.assertTrue(any("重复" in issue["message"] for issue in issues), repr([ascii(issue["message"]) for issue in issues]))
        with self.session_factory() as session:
            self.assertEqual(session.scalars(select(ObjectRecord)).all(), [])
        runs = await self.client.get(f"/api/data-sources/{source_id}/runs", headers=self.headers_for(self.editor))
        self.assertEqual(runs.json()[0]["status"], "failed")

    async def test_import_rejects_unknown_property_mapping_before_rows_are_written(self) -> None:
        source = await self.client.post(
            "/api/data-sources",
            headers=self.headers_for(self.editor),
            json={"ontology_id": str(self.ontology.id), "name": "无效映射"},
        )
        source_id = source.json()["id"]
        response = await self.client.put(
            f"/api/data-sources/{source_id}/mappings",
            headers=self.headers_for(self.editor),
            json={
                "object_type_api_name": "customer",
                "primary_key_field": "customer_id",
                "field_mappings": {"customer_id": "id", "full_name": "missing"},
            },
        )

        self.assertEqual(response.status_code, 422)
        self.assertIn("不存在", response.json()["detail"])

    async def test_viewer_cannot_create_data_source_connection(self) -> None:
        response = await self.client.post(
            "/api/data-sources",
            headers=self.headers_for(self.viewer),
            json={"ontology_id": str(self.ontology.id), "name": "未授权连接"},
        )

        self.assertEqual(response.status_code, 403)


if __name__ == "__main__":
    unittest.main()
