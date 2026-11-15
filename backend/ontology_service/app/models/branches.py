from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Integer, JSON, String, UniqueConstraint, Uuid, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.ontology_service.app.database import Base

json_document = JSON().with_variant(JSONB(), "postgresql")


class OntologyBranch(Base):
    __tablename__ = "ontology_branches"
    __table_args__ = (
        UniqueConstraint("ontology_id", "name", name="uq_ontology_branches_ontology_name"),
        CheckConstraint(
            "status IN ('active', 'proposed', 'merged', 'closed')",
            name="ck_ontology_branches_status",
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    ontology_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("ontologies.id", ondelete="CASCADE"), nullable=False, index=True
    )
    author_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    base_revision: Mapped[int] = mapped_column(Integer, nullable=False)
    base_snapshot: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict)
    snapshot: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict)
    changes: Mapped[list] = mapped_column(json_document, nullable=False, default=list)
    validation: Mapped[dict] = mapped_column(
        json_document, nullable=False, default=lambda: {"errors": [], "warnings": []}
    )
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="active", server_default="active")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    ontology: Mapped["Ontology"] = relationship()
    author: Mapped["User"] = relationship()
    proposals: Mapped[list["ChangeProposal"]] = relationship(back_populates="branch")


class ProposalResourceReview(Base):
    __tablename__ = "proposal_resource_reviews"
    __table_args__ = (
        UniqueConstraint("proposal_id", "resource_key", name="uq_proposal_resource_reviews_key"),
        CheckConstraint(
            "status IN ('pending', 'approved', 'rejected')",
            name="ck_proposal_resource_reviews_status",
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    proposal_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("change_proposals.id", ondelete="CASCADE"), nullable=False, index=True
    )
    resource_key: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="pending", server_default="pending")
    reviewer_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    comment: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    proposal: Mapped["ChangeProposal"] = relationship(back_populates="resource_reviews")
    reviewer: Mapped["User | None"] = relationship()
