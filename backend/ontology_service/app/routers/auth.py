from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Request, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models.projects import ProjectMembership
from backend.ontology_service.app.models.user import User
from backend.ontology_service.app.security import Actor, create_access_token, get_current_user, verify_password

router = APIRouter(prefix="/api/auth", tags=["身份认证"])


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=256)


class UserResponse(BaseModel):
    id: str
    email: str
    role: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
    project_id: str | None = None


@router.post("/login", response_model=LoginResponse)
def login(
    body: LoginRequest,
    request: Request,
    session: Annotated[Session, Depends(get_db)],
) -> LoginResponse:
    user = session.scalar(select(User).where(func.lower(User.email) == body.email.lower()))
    if user is None or not user.enabled or not verify_password(body.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="邮箱或密码不正确",
            headers={"WWW-Authenticate": "Bearer"},
        )
    actor = Actor(id=str(user.id), email=user.email, role=user.role)
    project_id = session.scalar(
        select(ProjectMembership.project_id)
        .where(ProjectMembership.user_id == user.id)
        .order_by(ProjectMembership.created_at, ProjectMembership.project_id)
        .limit(1)
    )
    return LoginResponse(
        access_token=create_access_token(actor, request.app.state.settings),
        user=UserResponse(id=actor.id, email=actor.email, role=actor.role),
        project_id=str(project_id) if project_id else None,
    )


@router.get("/me", response_model=UserResponse)
def me(actor: Annotated[Actor, Depends(get_current_user)]) -> UserResponse:
    return UserResponse(id=actor.id, email=actor.email, role=actor.role)
