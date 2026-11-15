from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import LinkType, ObjectType, Ontology
from backend.ontology_service.app.schemas.ontology import LinkTypeResponse, ObjectTypeResponse, OntologyCreate, OntologyResponse
from backend.ontology_service.app.security import Actor, get_current_user, require_role
from backend.ontology_service.app.services.audit import record_audit

router = APIRouter(prefix="/api", tags=["本体管理"])


@router.post("/ontology", response_model=OntologyResponse, status_code=status.HTTP_201_CREATED)
def create_ontology(
    body: OntologyCreate,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> OntologyResponse:
    ontology = Ontology(
        project_id=UUID(actor.project_id),
        api_name=body.api_name,
        display_name=body.display_name,
        description=body.description,
    )
    try:
        session.add(ontology)
        session.flush()
        record_audit(
            session,
            actor_id=actor.id,
            event_type="ontology.created",
            resource_type="ontology",
            resource_id=ontology.id,
            details={"api_name": ontology.api_name},
        )
        session.commit()
    except IntegrityError as exc:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="该项目中已存在同名本体 API") from exc
    return OntologyResponse(
        id=ontology.id,
        api_name=ontology.api_name,
        display_name=ontology.display_name,
        description=ontology.description,
        revision=ontology.revision,
        object_type_count=0,
        link_type_count=0,
    )


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
