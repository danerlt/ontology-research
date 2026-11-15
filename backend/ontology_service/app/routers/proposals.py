from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from backend.ontology_service.app.database import get_db
from backend.ontology_service.app.models import ChangeProposal, Ontology, OntologyBranch, ProposalResourceReview
from backend.ontology_service.app.schemas.proposals import (
    ProposalCreate,
    ProposalMergeResponse,
    ProposalReject,
    ProposalResourceReviewRequest,
    ProposalResourceReviewResponse,
    ProposalResponse,
)
from backend.ontology_service.app.security import Actor, require_role
from backend.ontology_service.app.services.audit import record_audit
from backend.ontology_service.app.services.governance import merge_proposal

router = APIRouter(prefix="/api/proposals", tags=["变更提案"])


@router.get("", response_model=list[ProposalResponse])
def list_proposals(
    _actor: Annotated[Actor, Depends(require_role("admin", "editor", "viewer"))],
    session: Annotated[Session, Depends(get_db)],
    ontology_id: UUID | None = None,
    proposal_status: str | None = None,
) -> list[ChangeProposal]:
    statement = (
        select(ChangeProposal)
        .options(selectinload(ChangeProposal.resource_reviews))
        .order_by(ChangeProposal.created_at.desc())
    )
    if ontology_id is not None:
        statement = statement.where(ChangeProposal.ontology_id == ontology_id)
    if proposal_status is not None:
        statement = statement.where(ChangeProposal.status == proposal_status)
    return list(session.scalars(statement).all())


@router.post("", response_model=ProposalResponse, status_code=status.HTTP_201_CREATED)
def create_proposal(
    body: ProposalCreate,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> ChangeProposal:
    ontology = session.get(Ontology, body.ontology_id)
    if ontology is None:
        raise HTTPException(status_code=404, detail="本体不存在")
    proposal = ChangeProposal(
        ontology_id=body.ontology_id,
        author_id=UUID(actor.id),
        title=body.title,
        description=body.description,
        base_revision=body.base_revision,
        changes=[change.model_dump(mode="json") for change in body.changes],
        status="draft",
    )
    session.add(proposal)
    session.flush()
    record_audit(
        session,
        actor_id=actor.id,
        event_type="schema.proposal.created",
        resource_type="proposal",
        resource_id=proposal.id,
        details={"ontology_id": str(body.ontology_id), "title": body.title},
    )
    session.commit()
    session.refresh(proposal)
    return proposal


@router.post(
    "/{proposal_id}/resources/{resource_key}/review",
    response_model=ProposalResourceReviewResponse,
)
def review_proposal_resource(
    proposal_id: UUID,
    resource_key: str,
    body: ProposalResourceReviewRequest,
    actor: Annotated[Actor, Depends(require_role("admin"))],
    session: Annotated[Session, Depends(get_db)],
) -> ProposalResourceReview:
    proposal = session.get(ChangeProposal, proposal_id)
    if proposal is None:
        raise HTTPException(status_code=404, detail="提案不存在")
    if proposal.status != "submitted":
        raise HTTPException(status_code=409, detail="只有待审提案可以评审")
    review = session.scalar(
        select(ProposalResourceReview).where(
            ProposalResourceReview.proposal_id == proposal_id,
            ProposalResourceReview.resource_key == resource_key,
        )
    )
    if review is None:
        raise HTTPException(status_code=404, detail="提案中不存在该变更资源")
    review.status = body.status
    review.reviewer_id = UUID(actor.id)
    review.comment = body.comment
    record_audit(
        session,
        actor_id=actor.id,
        event_type="schema.proposal.resource_reviewed",
        resource_type="proposal_resource",
        resource_id=review.id,
        details={"proposal_id": str(proposal.id), "resource_key": resource_key, "status": body.status},
    )
    session.commit()
    session.refresh(review)
    return review


@router.post("/{proposal_id}/submit", response_model=ProposalResponse)
def submit_proposal(
    proposal_id: UUID,
    actor: Annotated[Actor, Depends(require_role("admin", "editor"))],
    session: Annotated[Session, Depends(get_db)],
) -> ChangeProposal:
    proposal = session.get(ChangeProposal, proposal_id)
    if proposal is None:
        raise HTTPException(status_code=404, detail="提案不存在")
    if proposal.status != "draft":
        raise HTTPException(status_code=409, detail="只有草稿状态的提案可以提交")
    proposal.status = "submitted"
    record_audit(
        session,
        actor_id=actor.id,
        event_type="schema.proposal.submitted",
        resource_type="proposal",
        resource_id=proposal.id,
        details={"base_revision": proposal.base_revision},
    )
    session.commit()
    session.refresh(proposal)
    return proposal


@router.post("/{proposal_id}/merge", response_model=ProposalMergeResponse)
def merge_submitted_proposal(
    proposal_id: UUID,
    actor: Annotated[Actor, Depends(require_role("admin"))],
    session: Annotated[Session, Depends(get_db)],
) -> ProposalMergeResponse:
    proposal, revision = merge_proposal(session, proposal_id, actor)
    return ProposalMergeResponse(proposal=proposal, ontology_revision=revision)


@router.post("/{proposal_id}/reject", response_model=ProposalResponse)
def reject_submitted_proposal(
    proposal_id: UUID,
    body: ProposalReject,
    actor: Annotated[Actor, Depends(require_role("admin"))],
    session: Annotated[Session, Depends(get_db)],
) -> ChangeProposal:
    proposal = session.get(ChangeProposal, proposal_id)
    if proposal is None:
        raise HTTPException(status_code=404, detail="提案不存在")
    if proposal.status != "submitted":
        raise HTTPException(status_code=409, detail="只有已提交的提案可以驳回")
    proposal.status = "rejected"
    proposal.reviewer_id = UUID(actor.id)
    proposal.review_comment = body.reason
    if proposal.branch_id is not None:
        branch = session.get(OntologyBranch, proposal.branch_id)
        if branch is not None:
            branch.status = "active"
    record_audit(
        session,
        actor_id=actor.id,
        event_type="schema.proposal.rejected",
        resource_type="proposal",
        resource_id=proposal.id,
        details={"reason": body.reason},
    )
    session.commit()
    session.refresh(proposal)
    return proposal
