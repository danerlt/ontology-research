from datetime import timedelta
import unittest

from fastapi import Depends
from httpx import ASGITransport, AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.ontology_service.app.config import Settings
from backend.ontology_service.app.database import Base, get_db
from backend.ontology_service.app.main import create_app
from backend.ontology_service.app.models import Project, ProjectMembership
from backend.ontology_service.app.models.user import User
from backend.ontology_service.app.security import (
    Actor,
    create_access_token,
    hash_password,
    require_role,
)
from backend.ontology_service.app.routers.auth import LoginRequest


class AuthTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.engine = create_engine(
            "sqlite://",
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
        Base.metadata.create_all(self.engine)
        self.session_factory = sessionmaker(bind=self.engine, autoflush=False)
        self.settings = Settings(
            jwt_secret="unit-test-secret-long-enough-for-hmac-sha256",
            jwt_access_token_minutes=30,
        )
        self.app = create_app(self.settings)

        def override_get_db():
            with self.session_factory() as session:
                yield session

        self.app.dependency_overrides[get_db] = override_get_db
        with self.session_factory() as session:
            admin = User(email="admin@example.com", password_hash=hash_password("admin-pass"), role="admin")
            viewer = User(email="viewer@example.com", password_hash=hash_password("viewer-pass"), role="viewer")
            project = Project(api_name="auth_tests", display_name="认证测试项目")
            session.add_all([admin, viewer, project])
            session.flush()
            session.add_all([
                ProjectMembership(project_id=project.id, user_id=admin.id, role="admin"),
                ProjectMembership(project_id=project.id, user_id=viewer.id, role="viewer"),
            ])
            session.commit()
        self.client = AsyncClient(
            transport=ASGITransport(app=self.app),
            base_url="http://test",
        )

    async def asyncTearDown(self) -> None:
        await self.client.aclose()
        self.engine.dispose()

    def test_default_admin_email_is_accepted_by_login_schema(self) -> None:
        request = LoginRequest(email=self.settings.admin_email, password=self.settings.admin_password)

        self.assertEqual(request.email, "admin@example.com")

    async def test_login_returns_bearer_token(self) -> None:
        response = await self.client.post(
            "/api/auth/login",
            json={"email": "admin@example.com", "password": "admin-pass"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["token_type"], "bearer")
        self.assertTrue(response.json()["access_token"])
        self.assertEqual(response.json()["user"]["role"], "admin")
        self.assertTrue(response.json()["project_id"])

    async def test_invalid_credentials_are_rejected(self) -> None:
        response = await self.client.post(
            "/api/auth/login",
            json={"email": "admin@example.com", "password": "wrong"},
        )

        self.assertEqual(response.status_code, 401)

    async def test_expired_token_is_rejected(self) -> None:
        token = create_access_token(
            Actor(id="caa4d7cf-02c4-44c6-9889-8793459704e1", email="viewer@example.com", role="viewer"),
            self.settings,
            expires_delta=timedelta(seconds=-1),
        )

        response = await self.client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(response.status_code, 401)

    async def test_viewer_is_rejected_by_admin_dependency(self) -> None:
        @self.app.get("/test/admin-only")
        def admin_only(_actor: Actor = Depends(require_role("admin"))):
            return {"ok": True}

        login = await self.client.post(
            "/api/auth/login",
            json={"email": "viewer@example.com", "password": "viewer-pass"},
        )
        token = login.json()["access_token"]

        response = await self.client.get("/test/admin-only", headers={"Authorization": f"Bearer {token}"})

        self.assertEqual(response.status_code, 403)


if __name__ == "__main__":
    unittest.main()
