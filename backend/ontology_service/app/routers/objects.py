from typing import Annotated, Literal
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import (
    LinkType,
    ObjectLink,
    ObjectRecord,
    ObjectType,
    Ontology,
    PropertyDefinition,
)
from backend.ontology_service.app.schemas.objects import (
    ObjectCreate,
    ObjectLinkCreate,
    ObjectLinkResponse,
    ObjectListResponse,
    ObjectRecordResponse,
)
from backend.ontology_service.app.security import Actor, get_current_user, require_role
from backend.ontology_service.app.services.action_engine import validate_record_properties
from backend.ontology_service.app.services.audit import record_audit

router = APIRouter(prefix="/api/objects", tags=["对象数据"])


@router.get("", response_model=ObjectListResponse)
def list_objects(
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID | None = None,
    object_type_api_name: str | None = None,
    query: str | None = None,
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=25, ge=1, le=100),
    sort_by: Literal["created_at", "primary_key", "version"] = Query(default="created_at"),
    sort_order: Literal["asc", "desc"] = Query(default="desc"),
) -> ObjectListResponse:
    statement = select(ObjectRecord).join(ObjectType).options(selectinload(ObjectRecord.object_type))
    count_statement = select(func.count()).select_from(ObjectRecord).join(ObjectType)
    if ontology_id is not None:
        condition = ObjectType.ontology_id == ontology_id
        statement = statement.where(condition)
        count_statement = count_statement.where(condition)
    if object_type_api_name:
        condition = ObjectType.api_name == object_type_api_name
        statement = statement.where(condition)
        count_statement = count_statement.where(condition)
    if query:
        pattern = f"%{query}%"
        searchable_properties = session.scalars(
            select(PropertyDefinition.api_name)
            .join(ObjectType)
            .where(PropertyDefinition.data_type.in_(["string", "enum"]))
        ).all()
        search_conditions = [ObjectRecord.primary_key_value.ilike(pattern)]
        search_conditions.extend(
            ObjectRecord.properties[property_name].as_string().ilike(pattern)
            for property_name in searchable_properties
        )
        condition = or_(*search_conditions)
        statement = statement.where(condition)
        count_statement = count_statement.where(condition)
    total = session.scalar(count_statement) or 0
    sort_column = {
        "created_at": ObjectRecord.created_at,
        "primary_key": ObjectRecord.primary_key_value,
        "version": ObjectRecord.version,
    }[sort_by]
    ordering = sort_column.asc() if sort_order == "asc" else sort_column.desc()
    records = session.scalars(
        statement.order_by(ordering, ObjectRecord.id.asc()).offset((page - 1) * page_size).limit(page_size)
    ).all()
    return ObjectListResponse(
        items=[_record_response(record, actor_role=actor.role) for record in records],
        total=total,
        page=page,
        page_size=page_size,
    )


@router.post("", response_model=ObjectRecordResponse, status_code=status.HTTP_201_CREATED)
def create_object(
    body: ObjectCreate,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> ObjectRecordResponse:
    object_type = session.scalar(
        select(ObjectType).where(
            ObjectType.ontology_id == body.ontology_id,
            ObjectType.api_name == body.object_type_api_name,
        )
    )
    if object_type is None:
        raise HTTPException(status_code=404, detail="对象类型不存在")
    ontology = session.get(Ontology, body.ontology_id)
    if ontology is None:
        raise HTTPException(status_code=404, detail="本体不存在")

    properties = dict(body.properties)
    primary_key = object_type.primary_key_property
    if primary_key in properties and properties[primary_key] != body.primary_key_value:
        raise HTTPException(status_code=422, detail="主键属性值必须与对象主键一致")
    properties[primary_key] = body.primary_key_value
    validated = validate_record_properties(session, object_type, properties)
    record = ObjectRecord(
        object_type_id=object_type.id,
        primary_key_value=body.primary_key_value,
        properties=validated,
    )
    session.add(record)
    session.flush()
    record_audit(
        session,
        actor_id=actor.id,
        event_type="object.created",
        resource_type="object",
        resource_id=record.id,
        details={"object_type_api_name": object_type.api_name, "primary_key_value": record.primary_key_value},
    )
    session.commit()
    session.refresh(record)
    return _record_response(record, actor_role=actor.role)


@router.get("/{object_id}", response_model=ObjectRecordResponse)
def get_object(
    object_id: UUID,
    actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> ObjectRecordResponse:
    record = session.scalar(
        select(ObjectRecord)
        .where(ObjectRecord.id == object_id)
        .options(selectinload(ObjectRecord.object_type))
    )
    if record is None:
        raise HTTPException(status_code=404, detail="对象不存在")
    links = session.scalars(
        select(ObjectLink)
        .where(or_(ObjectLink.source_object_id == object_id, ObjectLink.target_object_id == object_id))
        .options(
            selectinload(ObjectLink.link_type),
            selectinload(ObjectLink.source_object).selectinload(ObjectRecord.object_type),
            selectinload(ObjectLink.target_object).selectinload(ObjectRecord.object_type),
        )
    ).all()
    return _record_response(record, actor_role=actor.role, links=links)


@router.post("/{object_id}/links", response_model=ObjectLinkResponse, status_code=status.HTTP_201_CREATED)
def create_object_link(
    object_id: UUID,
    body: ObjectLinkCreate,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> ObjectLinkResponse:
    source = session.scalar(
        select(ObjectRecord).where(ObjectRecord.id == object_id).options(selectinload(ObjectRecord.object_type))
    )
    target = session.scalar(
        select(ObjectRecord).where(ObjectRecord.id == body.target_object_id).options(selectinload(ObjectRecord.object_type))
    )
    if source is None or target is None:
        raise HTTPException(status_code=404, detail="链接中的对象不存在")
    link_type = session.scalar(
        select(LinkType).where(
            LinkType.ontology_id == source.object_type.ontology_id,
            LinkType.api_name == body.link_type_api_name,
        )
    )
    if link_type is None:
        raise HTTPException(status_code=404, detail="链接类型不存在")
    if link_type.source_type_id != source.object_type_id or link_type.target_type_id != target.object_type_id:
        raise HTTPException(status_code=422, detail="对象类型与链接方向不匹配")
    duplicate = session.scalar(
        select(ObjectLink.id).where(
            ObjectLink.link_type_id == link_type.id,
            ObjectLink.source_object_id == source.id,
            ObjectLink.target_object_id == target.id,
        )
    )
    if duplicate is not None:
        raise HTTPException(status_code=409, detail="此对象链接已存在")
    object_link = ObjectLink(
        link_type_id=link_type.id,
        source_object_id=source.id,
        target_object_id=target.id,
    )
    session.add(object_link)
    session.flush()
    record_audit(
        session,
        actor_id=actor.id,
        event_type="object.linked",
        resource_type="object_link",
        resource_id=object_link.id,
        details={"source_object_id": str(source.id), "target_object_id": str(target.id)},
    )
    session.commit()
    return ObjectLinkResponse(
        link_id=object_link.id,
        link_type_api_name=link_type.api_name,
        link_type_display_name=link_type.display_name,
        direction="outgoing",
        source_object_id=source.id,
        target_object_id=target.id,
        linked_object_id=target.id,
        linked_object_type_api_name=target.object_type.api_name,
        linked_object_type_display_name=target.object_type.display_name,
        linked_primary_key=target.primary_key_value,
    )


def _record_response(
    record: ObjectRecord,
    *,
    actor_role: str,
    links: list[ObjectLink] | None = None,
) -> ObjectRecordResponse:
    link_responses: list[ObjectLinkResponse] = []
    for object_link in links or []:
        outgoing = object_link.source_object_id == record.id
        linked_object = object_link.target_object if outgoing else object_link.source_object
        link_responses.append(
            ObjectLinkResponse(
                link_id=object_link.id,
                link_type_api_name=object_link.link_type.api_name,
                link_type_display_name=object_link.link_type.display_name,
                direction="outgoing" if outgoing else "incoming",
                source_object_id=object_link.source_object_id,
                target_object_id=object_link.target_object_id,
                linked_object_id=linked_object.id,
                linked_object_type_api_name=linked_object.object_type.api_name,
                linked_object_type_display_name=linked_object.object_type.display_name,
                linked_primary_key=linked_object.primary_key_value,
            )
        )
    properties = dict(record.properties)
    if actor_role == "viewer":
        sensitive_names = {
            definition.api_name
            for definition in record.object_type.properties
            if definition.sensitive
        }
        for property_name in sensitive_names:
            properties.pop(property_name, None)
    return ObjectRecordResponse(
        id=record.id,
        object_type_api_name=record.object_type.api_name,
        object_type_display_name=record.object_type.display_name,
        primary_key_value=record.primary_key_value,
        properties=properties,
        version=record.version,
        created_at=record.created_at,
        updated_at=record.updated_at,
        links=link_responses,
    )
