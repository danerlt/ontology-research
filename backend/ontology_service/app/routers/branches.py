from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import ChangeProposal, Ontology, OntologyBranch, ProposalResourceReview
from backend.ontology_service.app.schemas.branches import (
    BranchChanges,
    BranchProposalCreate,
    BranchValidationResponse,
    OntologyBranchCreate,
    OntologyBranchResponse,
)
from backend.ontology_service.app.schemas.proposals import ProposalResponse
from backend.ontology_service.app.security import Actor, get_current_user, require_role
from backend.ontology_service.app.services.audit import record_audit
from backend.ontology_service.app.services.branches import (
    apply_schema_changes,
    create_schema_snapshot,
    require_branch,
    resource_key_for_change,
)

router = APIRouter(prefix="/api/branches", tags=["Ontology 分支"])


@router.get("", response_model=list[OntologyBranchResponse])
def list_branches(
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID | None = None,
) -> list[OntologyBranch]:
    statement = select(OntologyBranch).order_by(OntologyBranch.updated_at.desc())
    if ontology_id is not None:
        statement = statement.where(OntologyBranch.ontology_id == ontology_id)
    return list(session.scalars(statement).all())


@router.post("", response_model=OntologyBranchResponse, status_code=status.HTTP_201_CREATED)
def create_branch(
    body: OntologyBranchCreate,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> OntologyBranch:
    ontology = session.scalar(select(Ontology).where(Ontology.id == body.ontology_id).with_for_update())
    if ontology is None:
        raise HTTPException(status_code=404, detail="本体不存在")
    snapshot = create_schema_snapshot(session, ontology)
    branch = OntologyBranch(
        ontology_id=ontology.id,
        author_id=UUID(actor.id),
        name=body.name,
        description=body.description,
        base_revision=ontology.revision,
        base_snapshot=snapshot,
        snapshot=snapshot,
        changes=[],
        validation={"errors": [], "warnings": [], "valid": True},
    )
    session.add(branch)
    try:
        session.flush()
        record_audit(
            session,
            actor_id=actor.id,
            event_type="schema.branch.created",
            resource_type="branch",
            resource_id=branch.id,
            details={"ontology_id": str(ontology.id), "base_revision": ontology.revision, "name": branch.name},
        )
        session.commit()
        session.refresh(branch)
    except IntegrityError as exc:
        session.rollback()
        raise HTTPException(status_code=409, detail="该本体中已存在同名分支") from exc
    return branch


@router.get("/{branch_id}", response_model=OntologyBranchResponse)
def get_branch(
    branch_id: UUID,
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> OntologyBranch:
    return require_branch(session, branch_id)


@router.post("/{branch_id}/changes", response_model=OntologyBranchResponse)
def add_branch_changes(
    branch_id: UUID,
    body: BranchChanges,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> OntologyBranch:
    branch = require_branch(session, branch_id, active=True)
    changes = [change.model_dump(mode="json", exclude_unset=True) for change in body.changes]
    branch.changes = [*branch.changes, *changes]
    branch.snapshot, branch.validation = apply_schema_changes(branch.base_snapshot, branch.changes)
    record_audit(
        session,
        actor_id=actor.id,
        event_type="schema.branch.changed",
        resource_type="branch",
        resource_id=branch.id,
        details={"change_count": len(changes), "validation_error_count": len(branch.validation["errors"])},
    )
    session.commit()
    session.refresh(branch)
    return branch


@router.post("/{branch_id}/validate", response_model=BranchValidationResponse)
def validate_branch(
    branch_id: UUID,
    _actor: Annotated[Actor, Depends(get_current_user)],
    session: Annotated[Session, Depends(get_db)],
) -> BranchValidationResponse:
    branch = require_branch(session, branch_id, active=True)
    branch.snapshot, branch.validation = apply_schema_changes(branch.base_snapshot, branch.changes)
    session.commit()
    return BranchValidationResponse(**branch.validation)


@router.post("/{branch_id}/rebase", response_model=OntologyBranchResponse)
def rebase_branch(
    branch_id: UUID,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> OntologyBranch:
    branch = require_branch(session, branch_id, active=True)
    ontology = session.scalar(select(Ontology).where(Ontology.id == branch.ontology_id).with_for_update())
    if ontology is None:
        raise HTTPException(status_code=404, detail="本体不存在")
    latest_snapshot = create_schema_snapshot(session, ontology)
    rebased_snapshot, validation = apply_schema_changes(latest_snapshot, branch.changes)
    if validation["errors"]:
        raise HTTPException(
            status_code=409,
            detail={"message": "分支与 main 存在资源冲突", "conflicts": validation["errors"]},
        )
    branch.base_revision = ontology.revision
    branch.base_snapshot = latest_snapshot
    branch.snapshot = rebased_snapshot
    branch.validation = validation
    record_audit(
        session,
        actor_id=actor.id,
        event_type="schema.branch.rebased",
        resource_type="branch",
        resource_id=branch.id,
        details={"base_revision": ontology.revision},
    )
    session.commit()
    session.refresh(branch)
    return branch


@router.post("/{branch_id}/propose", response_model=ProposalResponse, status_code=status.HTTP_201_CREATED)
def create_branch_proposal(
    branch_id: UUID,
    body: BranchProposalCreate,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> ChangeProposal:
    branch = require_branch(session, branch_id, active=True)
    if not branch.changes:
        raise HTTPException(status_code=422, detail="分支没有待提交的修改")
    branch.snapshot, branch.validation = apply_schema_changes(branch.base_snapshot, branch.changes)
    if branch.validation["errors"]:
        raise HTTPException(status_code=422, detail={"message": "本体检查未通过", **branch.validation})

    proposal = ChangeProposal(
        ontology_id=branch.ontology_id,
        branch_id=branch.id,
        author_id=UUID(actor.id),
        title=body.title,
        description=body.description,
        base_revision=branch.base_revision,
        changes=branch.changes,
        status="submitted",
    )
    resource_keys = sorted({resource_key_for_change(change) for change in branch.changes})
    proposal.resource_reviews = [
        ProposalResourceReview(resource_key=resource_key, status="pending") for resource_key in resource_keys
    ]
    branch.status = "proposed"
    session.add(proposal)
    session.flush()
    record_audit(
        session,
        actor_id=actor.id,
        event_type="schema.branch.proposed",
        resource_type="proposal",
        resource_id=proposal.id,
        details={"branch_id": str(branch.id), "resource_count": len(resource_keys)},
    )
    session.commit()
    session.refresh(proposal)
    return proposal


