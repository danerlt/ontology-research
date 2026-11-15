from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Annotated
from uuid import UUID

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pwdlib import PasswordHash
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models.projects import ProjectMembership
from backend.ontology_service.app.models.user import User

password_hash = PasswordHash.recommended()
bearer_scheme = HTTPBearer(auto_error=False)


@dataclass(frozen=True)
class Actor:
    id: str
    email: str
    role: str
    project_id: str | None = None


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(password: str, encoded_password: str) -> bool:
    try:
        return password_hash.verify(password, encoded_password)
    except (TypeError, ValueError):
        return False


def create_access_token(
    actor: Actor,
    settings,
    expires_delta: timedelta | None = None,
) -> str:
    now = datetime.now(timezone.utc)
    expires_at = now + (expires_delta or timedelta(minutes=settings.jwt_access_token_minutes))
    claims = {
        "sub": actor.id,
        "email": actor.email,
        "role": actor.role,
        "iat": now,
        "exp": expires_at,
    }
    return jwt.encode(claims, settings.jwt_secret, algorithm="HS256")


def get_authenticated_user(
    request: Request,
    credentials: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer_scheme)],
    session: Annotated[Session, Depends(get_db)],
) -> Actor:
    unauthorized = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="登录状态无效，请重新登录",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if credentials is None:
        raise unauthorized
    try:
        claims = jwt.decode(
            credentials.credentials,
            request.app.state.settings.jwt_secret,
            algorithms=["HS256"],
            options={"require": ["sub", "exp"]},
        )
        user_id = UUID(claims["sub"])
    except (jwt.InvalidTokenError, KeyError, TypeError, ValueError):
        raise unauthorized from None

    user = session.get(User, user_id)
    if user is None or not user.enabled:
        raise unauthorized
    return Actor(id=str(user.id), email=user.email, role=user.role)


def get_current_user(
    request: Request,
    actor: Annotated[Actor, Depends(get_authenticated_user)],
    session: Annotated[Session, Depends(get_db)],
) -> Actor:
    project_header = request.headers.get("X-Project-ID", "").strip()
    if project_header:
        try:
            project_id = UUID(project_header)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="当前项目标识无效") from None
        membership = session.scalar(
            select(ProjectMembership).where(
                ProjectMembership.project_id == project_id,
                ProjectMembership.user_id == UUID(actor.id),
            )
        )
        if membership is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="当前账号不属于所选项目")
    else:
        membership = session.scalar(
            select(ProjectMembership)
            .where(ProjectMembership.user_id == UUID(actor.id))
            .order_by(ProjectMembership.created_at, ProjectMembership.project_id)
        )
        if membership is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="当前账号尚未加入任何项目")
        project_id = membership.project_id

    session.info["project_id"] = project_id
    return Actor(
        id=actor.id,
        email=actor.email,
        role=membership.role,
        project_id=str(project_id),
    )


def require_role(*allowed_roles: str):
    def dependency(actor: Annotated[Actor, Depends(get_current_user)]) -> Actor:
        if actor.role not in allowed_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="当前账号没有此操作权限")
        return actor

    return dependency
