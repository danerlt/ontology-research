from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, UniqueConstraint, Uuid, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.ontology_service.app.database import Base

json_document = JSON().with_variant(JSONB(), "postgresql")


class ObjectRecord(Base):
    __tablename__ = "object_records"
    __table_args__ = (
        UniqueConstraint("object_type_id", "primary_key_value", name="uq_objects_type_primary_key"),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    object_type_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("object_types.id", ondelete="CASCADE"), nullable=False, index=True
    )
    primary_key_value: Mapped[str] = mapped_column(String(160), nullable=False)
    properties: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict, server_default="{}")
    version: Mapped[int] = mapped_column(Integer, nullable=False, default=1, server_default="1")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    object_type: Mapped["ObjectType"] = relationship()


class ObjectLink(Base):
    __tablename__ = "object_links"
    __table_args__ = (
        UniqueConstraint(
            "link_type_id", "source_object_id", "target_object_id", name="uq_object_links_endpoints"
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    link_type_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("link_types.id", ondelete="CASCADE"), nullable=False, index=True
    )
    source_object_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("object_records.id", ondelete="CASCADE"), nullable=False, index=True
    )
    target_object_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("object_records.id", ondelete="CASCADE"), nullable=False, index=True
    )
    properties: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict, server_default="{}")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    link_type: Mapped["LinkType"] = relationship()
    source_object: Mapped[ObjectRecord] = relationship(foreign_keys=[source_object_id])
    target_object: Mapped[ObjectRecord] = relationship(foreign_keys=[target_object_id])
