import unittest
from uuid import UUID

from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine, event, select
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.main import create_app
from backend.ontology_service.app.models import AuditEvent, ChangeProposal, ObjectType, Ontology, User
from backend.ontology_service.app.security import Actor, create_access_token, hash_password


class GovernanceApiTests(unittest.IsolatedAsyncioTestCase):
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

    async def create_and_submit(self, *, base_revision: int = 1, changes: list[dict] | None = None) -> str:
        proposal_changes = changes or [
            {
                "op": "add_object_type",
                "api_name": "site",
                "display_name": "站点",
                "description": "业务站点",
            }
        ]
        response = await self.client.post(
            "/api/proposals",
            headers=self.headers_for(self.editor),
            json={
                "ontology_id": str(self.ontology.id),
                "title": "新增站点类型",
                "description": "用于演示提案审阅",
                "base_revision": base_revision,
                "changes": proposal_changes,
            },
        )
        self.assertEqual(response.status_code, 201, response.text)
        proposal_id = response.json()["id"]
        submitted = await self.client.post(
            f"/api/proposals/{proposal_id}/submit",
            headers=self.headers_for(self.editor),
        )
        self.assertEqual(submitted.status_code, 200, submitted.text)
        return proposal_id

    async def test_editor_can_submit_object_type_proposal(self) -> None:
        proposal_id = await self.create_and_submit()

        with self.session_factory() as session:
            proposal = session.get(ChangeProposal, UUID(proposal_id))

        self.assertEqual(proposal.status, "submitted")

    async def test_editor_cannot_merge_schema_proposal(self) -> None:
        proposal_id = await self.create_and_submit()

        response = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.editor),
        )

        self.assertEqual(response.status_code, 403)
        with self.session_factory() as session:
            ontology = session.get(Ontology, self.ontology.id)
            proposal = session.get(ChangeProposal, UUID(proposal_id))
        self.assertEqual(ontology.revision, 1)
        self.assertEqual(proposal.status, "submitted")

    async def test_stale_schema_proposal_is_rejected(self) -> None:
        proposal_id = await self.create_and_submit(base_revision=0)

        response = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )

        self.assertEqual(response.status_code, 409)
        with self.session_factory() as session:
            ontology = session.get(Ontology, self.ontology.id)
        self.assertEqual(ontology.revision, 1)

    async def test_merge_increments_revision_and_writes_audit(self) -> None:
        proposal_id = await self.create_and_submit()

        response = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["ontology_revision"], 2)
        with self.session_factory() as session:
            ontology = session.get(Ontology, self.ontology.id)
            proposal = session.get(ChangeProposal, UUID(proposal_id))
            audit = session.scalar(
                select(AuditEvent).where(AuditEvent.event_type == "schema.proposal.merged")
            )
        self.assertEqual(ontology.revision, 2)
        self.assertEqual(proposal.status, "merged")
        self.assertEqual(audit.actor_id, self.admin.id)

    async def test_viewer_cannot_create_proposal(self) -> None:
        response = await self.client.post(
            "/api/proposals",
            headers=self.headers_for(self.viewer),
            json={
                "ontology_id": str(self.ontology.id),
                "title": "越权提案",
                "base_revision": 1,
                "changes": [{"op": "add_object_type", "api_name": "site", "display_name": "站点"}],
            },
        )

        self.assertEqual(response.status_code, 403)

    async def test_proposal_can_add_properties_and_links(self) -> None:
        proposal_id = await self.create_and_submit(
            changes=[
                {"op": "add_object_type", "api_name": "site", "display_name": "站点"},
                {"op": "add_object_type", "api_name": "asset", "display_name": "设备"},
                {
                    "op": "add_property",
                    "object_type_api_name": "site",
                    "api_name": "region",
                    "display_name": "区域",
                    "data_type": "string",
                    "required": True,
                },
                {
                    "op": "add_link_type",
                    "api_name": "site_assets",
                    "display_name": "站点设备",
                    "source_type_api_name": "site",
                    "target_type_api_name": "asset",
                },
            ]
        )

        response = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )
        object_types = await self.client.get(
            "/api/object-types",
            headers=self.headers_for(self.admin),
            params={"ontology_id": str(self.ontology.id)},
        )
        links = await self.client.get(
            "/api/link-types",
            headers=self.headers_for(self.admin),
            params={"ontology_id": str(self.ontology.id)},
        )

        self.assertEqual(response.status_code, 200, response.text)
        site = next(item for item in object_types.json() if item["api_name"] == "site")
        self.assertEqual(site["properties"][0]["api_name"], "region")
        self.assertEqual(links.json()[0]["api_name"], "site_assets")

    async def test_admin_can_reject_with_review_reason(self) -> None:
        proposal_id = await self.create_and_submit()

        response = await self.client.post(
            f"/api/proposals/{proposal_id}/reject",
            headers=self.headers_for(self.admin),
            json={"reason": "命名不符合约定"},
        )

        self.assertEqual(response.status_code, 200, response.text)
        self.assertEqual(response.json()["status"], "rejected")
        self.assertEqual(response.json()["review_comment"], "命名不符合约定")

    async def test_failed_merge_rolls_back_earlier_schema_changes(self) -> None:
        proposal_id = await self.create_and_submit(
            changes=[
                {"op": "add_object_type", "api_name": "site", "display_name": "站点"},
                {"op": "add_object_type", "api_name": "site", "display_name": "重复站点"},
            ]
        )

        response = await self.client.post(
            f"/api/proposals/{proposal_id}/merge",
            headers=self.headers_for(self.admin),
        )

        self.assertEqual(response.status_code, 409)
        with self.session_factory() as session:
            ontology = session.get(Ontology, self.ontology.id)
            object_types = session.scalars(select(ObjectType)).all()
        self.assertEqual(ontology.revision, 1)
        self.assertEqual(object_types, [])


if __name__ == "__main__":
    unittest.main()
