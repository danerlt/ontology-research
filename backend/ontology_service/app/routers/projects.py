from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models.projects import Project, ProjectMembership
from backend.ontology_service.app.models.user import User
from backend.ontology_service.app.schemas.projects import (
    ProjectCreate,
    ProjectMemberResponse,
    ProjectMemberUpsert,
    ProjectResponse,
)
from backend.ontology_service.app.security import Actor, get_authenticated_user, get_current_user, require_role
from backend.ontology_service.app.services.audit import record_audit

router = APIRouter(prefix="/api/projects", tags=["项目管理"])


@router.get("", response_model=list[ProjectResponse])
def list_projects(
    actor: Annotated[Actor, Depends(get_authenticated_user)],
    session: Annotated[Session, Depends(get_db)],
) -> list[ProjectResponse]:
    rows = session.execute(
        select(Project, ProjectMembership.role)
        .join(ProjectMembership, ProjectMembership.project_id == Project.id)
        .where(ProjectMembership.user_id == UUID(actor.id))
        .order_by(Project.display_name)
    ).all()
    return [
        ProjectResponse(
            id=project.id,
            api_name=project.api_name,
            display_name=project.display_name,
            description=project.description,
            role=role,
        )
        for project, role in rows
    ]


@router.post("", response_model=ProjectResponse, status_code=status.HTTP_201_CREATED)
def create_project(
    body: ProjectCreate,
    actor: Annotated[Actor, Depends(get_authenticated_user)],
    session: Annotated[Session, Depends(get_db)],
) -> ProjectResponse:
    if actor.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="只有系统管理员可以创建项目")
    project = Project(
        api_name=body.api_name,
        display_name=body.display_name,
        description=body.description,
        created_by_id=UUID(actor.id),
    )
    try:
        session.add(project)
        session.flush()
        session.add(ProjectMembership(project_id=project.id, user_id=UUID(actor.id), role="admin"))
        session.info["project_id"] = project.id
        record_audit(
            session,
            actor_id=actor.id,
            event_type="project.created",
            resource_type="project",
            resource_id=project.id,
            details={"api_name": project.api_name},
        )
        session.commit()
        session.refresh(project)
    except IntegrityError as exc:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="该项目 API 名称已存在") from exc
    return ProjectResponse(
        id=project.id,
        api_name=project.api_name,
        display_name=project.display_name,
        description=project.description,
        role="admin",
    )


@router.get("/{project_id}/members", response_model=list[ProjectMemberResponse])
def list_project_members(
    project_id: UUID,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> list[ProjectMemberResponse]:
    _require_active_project(actor, project_id)
    rows = session.execute(
        select(ProjectMembership, User)
        .join(User, User.id == ProjectMembership.user_id)
        .where(ProjectMembership.project_id == project_id)
        .order_by(User.email)
    ).all()
    return [
        ProjectMemberResponse(id=membership.id, user_id=user.id, email=user.email, role=membership.role)
        for membership, user in rows
    ]


@router.put("/{project_id}/members", response_model=ProjectMemberResponse)
def upsert_project_member(
    project_id: UUID,
    body: ProjectMemberUpsert,
    actor: Annotated[Actor, Depends(require_role("admin"))],
    session: Annotated[Session, Depends(get_db)],
) -> ProjectMemberResponse:
    _require_active_project(actor, project_id)
    user = session.scalar(select(User).where(User.email == body.email.lower(), User.enabled.is_(True)))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="未找到可用账号")
    membership = session.scalar(
        select(ProjectMembership).where(
            ProjectMembership.project_id == project_id,
            ProjectMembership.user_id == user.id,
        )
    )
    if membership is None:
        membership = ProjectMembership(project_id=project_id, user_id=user.id, role=body.role)
        session.add(membership)
    else:
        membership.role = body.role
    session.flush()
    record_audit(
        session,
        actor_id=actor.id,
        event_type="project.member.updated",
        resource_type="project_membership",
        resource_id=membership.id,
        details={"user_id": str(user.id), "email": user.email, "role": body.role},
    )
    session.commit()
    return ProjectMemberResponse(id=membership.id, user_id=user.id, email=user.email, role=membership.role)


def _require_active_project(actor: Actor, project_id: UUID) -> None:
    if actor.project_id != str(project_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="项目不存在")
