from typing import Any
from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.ontology_service.app.models import (
    ChangeProposal,
    ActionDefinition,
    LinkType,
    ObjectType,
    Ontology,
    OntologyBranch,
    PropertyDefinition,
    ProposalResourceReview,
)
from backend.ontology_service.app.security import Actor
from backend.ontology_service.app.services.audit import record_audit


def apply_schema_changes(session: Session, ontology_id: UUID, changes: list[dict[str, Any]]) -> None:
    for change in changes:
        operation = change["op"]
        if operation == "add_object_type":
            existing = session.scalar(
                select(ObjectType).where(
                    ObjectType.ontology_id == ontology_id,
                    ObjectType.api_name == change["api_name"],
                )
            )
            if existing is not None:
                raise HTTPException(status_code=409, detail="对象类型 API 名已存在")
            object_type = ObjectType(
                ontology_id=ontology_id,
                api_name=change["api_name"],
                display_name=change["display_name"],
                plural_display_name=change.get("plural_display_name") or change["display_name"],
                description=change.get("description", ""),
                primary_key_property=change.get("primary_key_property", "id"),
                title_key_property=change.get("title_key_property") or change.get("primary_key_property", "id"),
                aliases=change.get("aliases", []),
                groups=change.get("groups", []),
                icon=change.get("icon", "object"),
                icon_color=change.get("icon_color", "#4F8067"),
            )
            session.add(object_type)
            session.flush()
            session.add(
                PropertyDefinition(
                    object_type_id=object_type.id,
                    api_name=change.get("primary_key_property", "id"),
                    display_name="唯一标识",
                    data_type="string",
                    required=True,
                    editable=False,
                    unique_value=True,
                )
            )
            session.flush()
            continue

        if operation == "add_property":
            object_type = session.scalar(
                select(ObjectType).where(
                    ObjectType.ontology_id == ontology_id,
                    ObjectType.api_name == change["object_type_api_name"],
                )
            )
            if object_type is None:
                raise HTTPException(status_code=422, detail="目标对象类型不存在")
            existing = session.scalar(
                select(PropertyDefinition).where(
                    PropertyDefinition.object_type_id == object_type.id,
                    PropertyDefinition.api_name == change["api_name"],
                )
            )
            if existing is not None:
                raise HTTPException(status_code=409, detail="属性 API 名已存在")
            session.add(
                PropertyDefinition(
                    object_type_id=object_type.id,
                    api_name=change["api_name"],
                    display_name=change["display_name"],
                    data_type=change["data_type"],
                    required=change.get("required", False),
                    editable=change.get("editable", True),
                    unique_value=change.get("unique_value", False),
                    sensitive=change.get("sensitive", False),
                    options=change.get("options", {}),
                )
            )
            session.flush()
            continue

        if operation == "update_object_type":
            object_type = session.scalar(
                select(ObjectType).where(
                    ObjectType.ontology_id == ontology_id,
                    ObjectType.api_name == change["api_name"],
                )
            )
            if object_type is None:
                raise HTTPException(status_code=422, detail="待修改的对象类型不存在")
            for field in (
                "display_name",
                "plural_display_name",
                "description",
                "title_key_property",
                "aliases",
                "groups",
                "icon",
                "icon_color",
            ):
                if field in change:
                    setattr(object_type, field, change[field])
            session.flush()
            continue

        if operation == "update_property":
            object_type = session.scalar(
                select(ObjectType).where(
                    ObjectType.ontology_id == ontology_id,
                    ObjectType.api_name == change["object_type_api_name"],
                )
            )
            if object_type is None:
                raise HTTPException(status_code=422, detail="待修改属性所属的对象类型不存在")
            prop = session.scalar(
                select(PropertyDefinition).where(
                    PropertyDefinition.object_type_id == object_type.id,
                    PropertyDefinition.api_name == change["api_name"],
                )
            )
            if prop is None:
                raise HTTPException(status_code=422, detail="待修改的属性不存在")
            for field in (
                "display_name",
                "data_type",
                "required",
                "editable",
                "unique_value",
                "sensitive",
                "options",
            ):
                if field in change:
                    setattr(prop, field, change[field])
            session.flush()
            continue

        if operation == "add_link_type":
            source_type = session.scalar(
                select(ObjectType).where(
                    ObjectType.ontology_id == ontology_id,
                    ObjectType.api_name == change["source_type_api_name"],
                )
            )
            target_type = session.scalar(
                select(ObjectType).where(
                    ObjectType.ontology_id == ontology_id,
                    ObjectType.api_name == change["target_type_api_name"],
                )
            )
            if source_type is None or target_type is None:
                raise HTTPException(status_code=422, detail="链接两端的对象类型必须存在于同一本体")
            existing = session.scalar(
                select(LinkType).where(
                    LinkType.ontology_id == ontology_id,
                    LinkType.api_name == change["api_name"],
                )
            )
            if existing is not None:
                raise HTTPException(status_code=409, detail="链接类型 API 名已存在")
            session.add(
                LinkType(
                    ontology_id=ontology_id,
                    api_name=change["api_name"],
                    display_name=change["display_name"],
                    description=change.get("description", ""),
                    source_type_id=source_type.id,
                    target_type_id=target_type.id,
                )
            )
            session.flush()
            continue

        if operation == "update_link_type":
            link = session.scalar(
                select(LinkType).where(
                    LinkType.ontology_id == ontology_id,
                    LinkType.api_name == change["api_name"],
                )
            )
            if link is None:
                raise HTTPException(status_code=422, detail="待修改的链接类型不存在")
            for field in ("display_name", "description"):
                if field in change:
                    setattr(link, field, change[field])
            session.flush()
            continue

        if operation == "add_action":
            object_type = session.scalar(
                select(ObjectType).where(
                    ObjectType.ontology_id == ontology_id,
                    ObjectType.api_name == change["object_type_api_name"],
                )
            )
            if object_type is None:
                raise HTTPException(status_code=422, detail="Action 目标对象类型不存在")
            existing = session.scalar(
                select(ActionDefinition).where(
                    ActionDefinition.ontology_id == ontology_id,
                    ActionDefinition.api_name == change["api_name"],
                )
            )
            if existing is not None:
                raise HTTPException(status_code=409, detail="Action API 名已存在")
            session.add(
                ActionDefinition(
                    ontology_id=ontology_id,
                    object_type_id=object_type.id,
                    api_name=change["api_name"],
                    display_name=change["display_name"],
                    description=change.get("description", ""),
                    allowed_properties=change["allowed_properties"],
                    parameters_schema=change.get("parameters_schema", {}),
                    submission_criteria=change.get("submission_criteria", {}),
                    enabled=change.get("enabled", True),
                )
            )
            session.flush()
            continue

        if operation == "update_action":
            action = session.scalar(
                select(ActionDefinition).where(
                    ActionDefinition.ontology_id == ontology_id,
                    ActionDefinition.api_name == change["api_name"],
                )
            )
            if action is None:
                raise HTTPException(status_code=422, detail="待修改的 Action 不存在")
            for field in (
                "display_name",
                "description",
                "allowed_properties",
                "parameters_schema",
                "submission_criteria",
                "enabled",
            ):
                if field in change:
                    setattr(action, field, change[field])
            session.flush()
            continue

        raise HTTPException(status_code=422, detail=f"不支持的本体变更类型：{operation}")


def merge_proposal(session: Session, proposal_id: UUID, actor: Actor) -> tuple[ChangeProposal, int]:
    proposal = session.get(ChangeProposal, proposal_id)
    if proposal is None:
        raise HTTPException(status_code=404, detail="提案不存在")
    if proposal.status != "submitted":
        raise HTTPException(status_code=409, detail="只有已提交的提案可以合并")
    branch = None
    if proposal.branch_id is not None:
        branch = session.get(OntologyBranch, proposal.branch_id)
        reviews = session.scalars(
            select(ProposalResourceReview).where(ProposalResourceReview.proposal_id == proposal.id)
        ).all()
        if branch is None or branch.status != "proposed":
            raise HTTPException(status_code=409, detail="本体分支不处于待合并状态")
        if not reviews or any(review.status != "approved" for review in reviews):
            raise HTTPException(status_code=409, detail="所有变更资源都必须通过评审后才能合并")
    ontology = session.scalar(
        select(Ontology).where(Ontology.id == proposal.ontology_id).with_for_update()
    )
    if ontology is None:
        raise HTTPException(status_code=404, detail="本体不存在")
    if proposal.base_revision != ontology.revision:
        raise HTTPException(status_code=409, detail="提案基于旧版本，请重新基于当前版本提交")

    try:
        with session.begin_nested():
            apply_schema_changes(session, ontology.id, proposal.changes)
            ontology.revision += 1
            proposal.status = "merged"
            proposal.reviewer_id = UUID(actor.id)
            if branch is not None:
                branch.status = "merged"
            record_audit(
                session,
                actor_id=actor.id,
                event_type="schema.proposal.merged",
                resource_type="proposal",
                resource_id=proposal.id,
                details={"ontology_id": str(ontology.id), "revision": ontology.revision},
            )
            session.flush()
    except HTTPException:
        raise
    except IntegrityError as exc:
        raise HTTPException(status_code=409, detail="本体变更未能合并，请检查版本和名称冲突") from exc

    session.commit()
    session.refresh(proposal)
    return proposal, ontology.revision
