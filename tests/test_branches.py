import unittest
from uuid import UUID

from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine, event, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.main import create_app
from backend.ontology_service.app.models import ObjectType, Ontology, User
from backend.ontology_service.app.security import Actor, create_access_token, hash_password


class OntologyBranchApiTests(unittest.IsolatedAsyncioTestCase):
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
        self.ontology = Ontology(api_name="operations", display_name="运营本体", revision=1)
        with self.session_factory() as session:
            session.add_all([self.admin, self.editor, self.ontology])
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

    async def create_branch(self) -> str:
        response = await self.client.post(
            "/api/branches",
            headers=self.headers_for(self.editor),
            json={"ontology_id": str(self.ontology.id), "name": "customer-work", "description": "客户模型调整"},
        )
        self.assertEqual(response.status_code, 201, response.text)
        return response.json()["id"]

    async def stage(self, branch_id: str, changes: list[dict]) -> None:
        response = await self.client.post(
            f"/api/branches/{branch_id}/changes",
            headers=self.headers_for(self.editor),
            json={"changes": changes},
        )
        self.assertEqual(response.status_code, 200, response.text)

    async def propose(self, branch_id: str) -> str:
        response = await self.client.post(
            f"/api/branches/{branch_id}/propose",
            headers=self.headers_for(self.editor),
            json={"title": "新增站点类型", "description": "建立站点语义"},
        )
        self.assertEqual(response.status_code, 201, response.text)
        return response.json()["id"]

    async def test_branch_changes_do_not_mutate_main_schema(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )

        main_types = await self.client.get(
            "/api/object-types",
            headers=self.headers_for(self.editor),
            params={"ontology_id": str(self.ontology.id)},
        )
        branch = await self.client.get(f"/api/branches/{branch_id}", headers=self.headers_for(self.editor))

        self.assertEqual(main_types.status_code, 200)
        self.assertEqual(main_types.json(), [])
        self.assertEqual(branch.status_code, 200)
        self.assertIn("site", {item["api_name"] for item in branch.json()["snapshot"]["object_types"]})

    async def test_branch_validation_reports_duplicate_api_name(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [
                {"op": "add_object_type", "api_name": "site", "display_name": "站点"},
                {"op": "add_object_type", "api_name": "site", "display_name": "重复站点"},
            ],
        )

        response = await self.client.post(
            f"/api/branches/{branch_id}/validate",
            headers=self.headers_for(self.editor),
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertTrue(any("site" in issue["path"] for issue in response.json()["errors"]))

    async def test_merge_rejects_stale_branch_without_partial_writes(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )
        proposal_id = await self.propose(branch_id)
        with self.session_factory() as session:
            ontology = session.get(Ontology, self.ontology.id)
            ontology.revision += 1
            session.commit()

        response = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )

        self.assertEqual(response.status_code, 409)
        with self.session_factory() as session:
            ontology = session.get(Ontology, self.ontology.id)
            site = session.scalar(select(ObjectType).where(ObjectType.api_name == "site"))
        self.assertEqual(ontology.revision, 2)
        self.assertIsNone(site)

    async def test_resource_review_required_before_merge(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )
        proposal_id = await self.propose(branch_id)
        merge_before_review = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )
        self.assertEqual(merge_before_review.status_code, 409)

        review = await self.client.post(
            f"/api/proposals/{proposal_id}/resources/object_type:site/review",
            headers=self.headers_for(self.admin),
            json={"status": "approved", "comment": "字段定义符合约定"},
        )
        merge_after_review = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )

        self.assertEqual(review.status_code, 200, review.text)
        self.assertEqual(merge_after_review.status_code, 200, merge_after_review.text)
        with self.session_factory() as session:
            site = session.scalar(select(ObjectType).where(ObjectType.api_name == "site"))
        self.assertIsNotNone(site)

    async def test_rebase_preserves_branch_changes_and_updates_base_revision(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )
        with self.session_factory() as session:
            session.add(ObjectType(ontology_id=self.ontology.id, api_name="customer", display_name="客户"))
            session.get(Ontology, self.ontology.id).revision = 2
            session.commit()

        response = await self.client.post(
            f"/api/branches/{branch_id}/rebase",
            headers=self.headers_for(self.editor),
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["base_revision"], 2)
        self.assertEqual(
            {item["api_name"] for item in response.json()["snapshot"]["object_types"]},
            {"customer", "site"},
        )

    async def test_rebase_reports_resource_conflict_without_changing_branch(self) -> None:
        branch_id = await self.create_branch()
        await self.stage(
            branch_id,
            [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
        )
        with self.session_factory() as session:
            session.add(ObjectType(ontology_id=self.ontology.id, api_name="site", display_name="已占用站点"))
            session.get(Ontology, self.ontology.id).revision = 2
            session.commit()

        response = await self.client.post(
            f"/api/branches/{branch_id}/rebase",
            headers=self.headers_for(self.editor),
        )

        self.assertEqual(response.status_code, 409)
        self.assertIn("object_type:site", response.json()["detail"]["conflicts"][0]["path"])
        branch = await self.client.get(f"/api/branches/{branch_id}", headers=self.headers_for(self.editor))
        self.assertEqual(branch.json()["base_revision"], 1)


if __name__ == "__main__":
    unittest.main()
