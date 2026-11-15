from typing import Annotated, Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import ObjectType, Ontology, OntologyBranch
from backend.ontology_service.app.schemas.derived_properties import (
    DerivedPropertyPreviewRequest,
    DerivedPropertyPreviewResponse,
)
from backend.ontology_service.app.security import Actor, get_current_user
from backend.ontology_service.app.services.branches import create_schema_snapshot
from backend.ontology_service.app.services.derived_property_engine import preview_derived_property

router = APIRouter(prefix="/api/derived-properties", tags=["派生属性"])


@router.get("")
def list_derived_properties(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID,
) -> list[dict[str, Any]]:
    object_types = session.scalars(
        select(ObjectType)
        .where(ObjectType.ontology_id == ontology_id)
        .options(selectinload(ObjectType.properties))
        .order_by(ObjectType.api_name)
    ).all()
    results = []
    for object_type in object_types:
        for prop in object_type.properties:
            definition = prop.options.get("derived_property")
            if definition:
                results.append({
                    "object_type_api_name": object_type.api_name,
                    "object_type_display_name": object_type.display_name,
                    "api_name": prop.api_name,
                    "display_name": prop.display_name,
                    "data_type": prop.data_type,
                    "sensitive": prop.sensitive,
                    "definition": definition,
                })
    return results


@router.post("/preview", response_model=DerivedPropertyPreviewResponse)
def preview_derived_property_route(
    body: DerivedPropertyPreviewRequest,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> dict[str, Any]:
    ontology = session.get(Ontology, body.ontology_id)
    if ontology is None:
        raise HTTPException(status_code=404, detail="本体不存在")
    snapshot = create_schema_snapshot(session, ontology)
    if body.branch_id is not None:
        branch = session.get(OntologyBranch, body.branch_id)
        if branch is None or branch.ontology_id != ontology.id:
            raise HTTPException(status_code=404, detail="本体分支不存在")
        snapshot = branch.snapshot
    return preview_derived_property(
        session,
        ontology_id=ontology.id,
        object_id=body.object_id,
        definition=body.definition,
        actor_role=actor.role,
        snapshot=snapshot,
    )
