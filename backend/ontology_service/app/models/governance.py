from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    JSON,
    String,
    UniqueConstraint,
    Uuid,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.ontology_service.app.database import Base

json_document = JSON().with_variant(JSONB(), "postgresql")


class ActionDefinition(Base):
    __tablename__ = "action_definitions"
    __table_args__ = (
        UniqueConstraint("ontology_id", "api_name", name="uq_actions_ontology_api_name"),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    ontology_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("ontologies.id", ondelete="CASCADE"), nullable=False, index=True
    )
    object_type_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("object_types.id", ondelete="CASCADE"), nullable=False, index=True
    )
    api_name: Mapped[str] = mapped_column(String(80), nullable=False)
    display_name: Mapped[str] = mapped_column(String(160), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    allowed_properties: Mapped[list] = mapped_column(json_document, nullable=False, default=list)
    parameters_schema: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict)
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    object_type: Mapped["ObjectType"] = relationship()


class ChangeProposal(Base):
    __tablename__ = "change_proposals"
    __table_args__ = (
        CheckConstraint(
            "status IN ('draft', 'submitted', 'merged', 'rejected')",
            name="ck_change_proposals_status",
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    ontology_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("ontologies.id", ondelete="CASCADE"), nullable=False, index=True
    )
    author_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    reviewer_id: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    title: Mapped[str] = mapped_column(String(240), nullable=False)
    description: Mapped[str] = mapped_column(String(4000), default="", nullable=False)
    base_revision: Mapped[int] = mapped_column(Integer, nullable=False)
    changes: Mapped[list] = mapped_column(json_document, nullable=False, default=list)
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="draft", server_default="draft")
    review_comment: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    ontology: Mapped["Ontology"] = relationship()
    author: Mapped["User"] = relationship(foreign_keys=[author_id])
    reviewer: Mapped["User | None"] = relationship(foreign_keys=[reviewer_id])
