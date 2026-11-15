import unittest
from uuid import UUID, uuid4

from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.main import create_app
from backend.ontology_service.app.models import ObjectRecord, ObjectType, Ontology, Project, ProjectMembership, User
from backend.ontology_service.app.security import Actor, create_access_token, hash_password


class ProjectScopeApiTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine, autoflush=False, expire_on_commit=False)
        self.settings = Settings(jwt_secret="unit-test-secret-long-enough-for-hmac-sha256")
        self.admin = User(email="admin@example.com", password_hash=hash_password("admin-pass"), role="admin")
        self.viewer = User(email="viewer@example.com", password_hash=hash_password("viewer-pass"), role="admin")
        self.project_a = Project(id=uuid4(), api_name="fulfillment", display_name="履约项目")
        self.project_b = Project(id=uuid4(), api_name="finance", display_name="财务项目")
        with self.session_factory() as session:
            session.add_all([self.admin, self.viewer, self.project_a, self.project_b])
            session.flush()
            self.ontology_a = Ontology(
                project_id=self.project_a.id,
                api_name="fulfillment_model",
                display_name="履约本体",
            )
            self.ontology_b = Ontology(
                project_id=self.project_b.id,
                api_name="finance_model",
                display_name="财务本体",
            )
            session.add_all(
                [
                    self.ontology_a,
                    self.ontology_b,
                    ProjectMembership(project_id=self.project_a.id, user_id=self.admin.id, role="admin"),
                    ProjectMembership(project_id=self.project_b.id, user_id=self.admin.id, role="admin"),
                    ProjectMembership(project_id=self.project_a.id, user_id=self.viewer.id, role="viewer"),
                ]
            )
            session.flush()
            type_b = ObjectType(
                ontology_id=self.ontology_b.id,
                api_name="account",
                display_name="财务账户",
            )
            session.add(type_b)
            session.flush()
            self.record_b = ObjectRecord(
                object_type_id=type_b.id,
                primary_key_value="A-7",
                properties={"name": "受限账户"},
            )
            session.add(self.record_b)
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

    def headers_for(self, user: User, project_id: UUID | None = None) -> dict[str, str]:
        actor = Actor(id=str(user.id), email=user.email, role=user.role)
        headers = {"Authorization": f"Bearer {create_access_token(actor, self.settings)}"}
        if project_id:
            headers["X-Project-ID"] = str(project_id)
        return headers

    async def test_user_sees_only_projects_they_belong_to(self) -> None:
        response = await self.client.get("/api/projects", headers=self.headers_for(self.viewer))

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual([item["api_name"] for item in response.json()], ["fulfillment"])
        self.assertEqual(response.json()[0]["role"], "viewer")

    async def test_active_project_limits_ontology_list(self) -> None:
        response = await self.client.get(
            "/api/ontology",
            headers=self.headers_for(self.viewer, self.project_a.id),
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual([item["api_name"] for item in response.json()], ["fulfillment_model"])

    async def test_non_member_cannot_select_another_project(self) -> None:
        response = await self.client.get(
            "/api/ontology",
            headers=self.headers_for(self.viewer, self.project_b.id),
        )

        self.assertEqual(response.status_code, 403)

    async def test_project_scope_hides_foreign_object_ids(self) -> None:
        response = await self.client.get(
            f"/api/objects/{self.record_b.id}",
            headers=self.headers_for(self.viewer, self.project_a.id),
        )

        self.assertEqual(response.status_code, 404)
        self.assertNotIn("受限账户", response.text)

    async def test_project_member_role_overrides_global_user_role(self) -> None:
        response = await self.client.post(
            "/api/ontology",
            headers=self.headers_for(self.viewer, self.project_a.id),
            json={"api_name": "forbidden_model", "display_name": "不应创建", "description": ""},
        )

        self.assertEqual(response.status_code, 403)

    async def test_project_creation_grants_creator_admin_membership(self) -> None:
        response = await self.client.post(
            "/api/projects",
            headers=self.headers_for(self.admin),
            json={"api_name": "supply_chain", "display_name": "供应链", "description": "跨系统供应链本体"},
        )

        self.assertEqual(response.status_code, 201, response.text)
        self.assertEqual(response.json()["role"], "admin")
        listed = await self.client.get("/api/projects", headers=self.headers_for(self.admin))
        self.assertIn("supply_chain", {item["api_name"] for item in listed.json()})

    async def test_project_admin_can_add_existing_user_as_member(self) -> None:
        response = await self.client.put(
            f"/api/projects/{self.project_a.id}/members",
            headers=self.headers_for(self.admin, self.project_a.id),
            json={"email": self.viewer.email, "role": "editor"},
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["role"], "editor")
        projects = await self.client.get("/api/projects", headers=self.headers_for(self.viewer))
        self.assertEqual([item["api_name"] for item in projects.json()], ["fulfillment"])
        self.assertEqual(projects.json()[0]["role"], "editor")

    async def test_project_member_can_create_another_ontology(self) -> None:
        response = await self.client.post(
            "/api/ontology",
            headers=self.headers_for(self.admin, self.project_a.id),
            json={"api_name": "inventory_model", "display_name": "库存本体", "description": "商品和库存"},
        )

        self.assertEqual(response.status_code, 201, response.text)
        ontologies = await self.client.get(
            "/api/ontology",
            headers=self.headers_for(self.admin, self.project_a.id),
        )
        self.assertEqual({item["api_name"] for item in ontologies.json()}, {"fulfillment_model", "inventory_model"})

    async def test_ontology_api_name_is_unique_within_each_project(self) -> None:
        response = await self.client.post(
            "/api/ontology",
            headers=self.headers_for(self.admin, self.project_b.id),
            json={"api_name": "fulfillment_model", "display_name": "财务侧履约视图", "description": "同名资源属于不同项目"},
        )

        self.assertEqual(response.status_code, 201, response.text)


if __name__ == "__main__":
    unittest.main()
