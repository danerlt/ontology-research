from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import ActionDefinition, ObjectRecord
from backend.ontology_service.app.schemas.objects import (
    ActionDefinitionResponse,
    ActionExecuteRequest,
    ObjectRecordResponse,
)
from backend.ontology_service.app.security import Actor, get_current_user, require_role
from backend.ontology_service.app.services.action_engine import execute_action
from backend.ontology_service.app.routers.objects import _record_response

router = APIRouter(prefix="/api/actions", tags=["Action 操作"])


@router.get("", response_model=list[ActionDefinitionResponse])
def list_actions(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID | None = None,
    object_type_api_name: str | None = None,
) -> list[ActionDefinitionResponse]:
    statement = select(ActionDefinition).options(selectinload(ActionDefinition.object_type))
    if ontology_id is not None:
        statement = statement.where(ActionDefinition.ontology_id == ontology_id)
    if object_type_api_name is not None:
        statement = statement.join(ActionDefinition.object_type).where(
            ActionDefinition.object_type.has(api_name=object_type_api_name)
        )
    actions = session.scalars(statement.order_by(ActionDefinition.display_name)).all()
    return [
        ActionDefinitionResponse(
            id=action.id,
            api_name=action.api_name,
            display_name=action.display_name,
            description=action.description,
            object_type_api_name=action.object_type.api_name,
            allowed_properties=action.allowed_properties,
            parameters_schema=action.parameters_schema,
            enabled=action.enabled,
        )
        for action in actions
    ]


@router.post("/{action_api_name}/execute", response_model=ObjectRecordResponse)
def run_action(
    action_api_name: str,
    body: ActionExecuteRequest,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> ObjectRecordResponse:
    record = session.scalar(
        select(ObjectRecord)
        .where(ObjectRecord.id == body.object_id)
        .options(selectinload(ObjectRecord.object_type))
    )
    if record is None:
        raise HTTPException(status_code=404, detail="对象不存在")
    action = session.scalar(
        select(ActionDefinition)
        .where(
            ActionDefinition.api_name == action_api_name,
            ActionDefinition.object_type_id == record.object_type_id,
        )
        .options(selectinload(ActionDefinition.object_type))
    )
    if action is None:
        raise HTTPException(status_code=404, detail="Action 不存在或不适用于此对象")
    updated = execute_action(
        session,
        action,
        record,
        body.parameters,
        expected_version=body.expected_version,
        actor=actor,
    )
    return _record_response(updated, actor_role=actor.role)
