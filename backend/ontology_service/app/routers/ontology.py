from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import LinkType, ObjectType, Ontology
from backend.ontology_service.app.schemas.ontology import LinkTypeResponse, ObjectTypeResponse, OntologyResponse
from backend.ontology_service.app.security import Actor, get_current_user

router = APIRouter(prefix="/api", tags=["本体管理"])


@router.get("/ontology", response_model=list[OntologyResponse])
def list_ontologies(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> list[OntologyResponse]:
    ontologies = session.scalars(select(Ontology).order_by(Ontology.display_name)).all()
    return [
        OntologyResponse(
            id=ontology.id,
            api_name=ontology.api_name,
            display_name=ontology.display_name,
            description=ontology.description,
            revision=ontology.revision,
            object_type_count=session.scalar(
                select(func.count()).select_from(ObjectType).where(ObjectType.ontology_id == ontology.id)
            )
            or 0,
            link_type_count=session.scalar(
                select(func.count()).select_from(LinkType).where(LinkType.ontology_id == ontology.id)
            )
            or 0,
        )
        for ontology in ontologies
    ]


@router.get("/object-types", response_model=list[ObjectTypeResponse])
def list_object_types(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID | None = None,
) -> list[ObjectTypeResponse]:
    statement = select(ObjectType).options(selectinload(ObjectType.properties)).order_by(ObjectType.display_name)
    if ontology_id is not None:
        statement = statement.where(ObjectType.ontology_id == ontology_id)
    return list(session.scalars(statement).all())


@router.get("/link-types", response_model=list[LinkTypeResponse])
def list_link_types(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID | None = None,
) -> list[LinkTypeResponse]:
    statement = select(LinkType).order_by(LinkType.display_name)
    if ontology_id is not None:
        statement = statement.where(LinkType.ontology_id == ontology_id)
    return list(session.scalars(statement).all())
