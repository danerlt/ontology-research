from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, UniqueConstraint, Uuid, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.ontology_service.app.database import Base

json_document = JSON().with_variant(JSONB(), "postgresql")


class DataSourceConnection(Base):
    __tablename__ = "data_source_connections"
    __table_args__ = (UniqueConstraint("ontology_id", "name", name="uq_data_sources_ontology_name"),)

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    ontology_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("ontologies.id", ondelete="CASCADE"), nullable=False, index=True
    )
    created_by_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    name: Mapped[str] = mapped_column(String(160), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    connector_type: Mapped[str] = mapped_column(String(24), default="local_file", nullable=False)
    status: Mapped[str] = mapped_column(String(16), default="ready", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    ontology: Mapped["Ontology"] = relationship()
    created_by: Mapped["User"] = relationship()
    mappings: Mapped[list["DataSourceMapping"]] = relationship(
        back_populates="connection", cascade="all, delete-orphan", order_by="DataSourceMapping.created_at"
    )
    runs: Mapped[list["DataImportRun"]] = relationship(
        back_populates="connection", cascade="all, delete-orphan", order_by="DataImportRun.created_at.desc()"
    )


class DataSourceMapping(Base):
    __tablename__ = "data_source_mappings"
    __table_args__ = (
        UniqueConstraint("connection_id", "object_type_id", name="uq_data_source_mappings_type"),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    connection_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("data_source_connections.id", ondelete="CASCADE"), nullable=False, index=True
    )
    object_type_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("object_types.id", ondelete="CASCADE"), nullable=False, index=True
    )
    primary_key_field: Mapped[str] = mapped_column(String(160), nullable=False)
    field_mappings: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    connection: Mapped[DataSourceConnection] = relationship(back_populates="mappings")
    object_type: Mapped["ObjectType"] = relationship()


class DataImportRun(Base):
    __tablename__ = "data_import_runs"

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    connection_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("data_source_connections.id", ondelete="CASCADE"), nullable=False, index=True
    )
    mapping_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("data_source_mappings.id", ondelete="CASCADE"), nullable=False, index=True
    )
    actor_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    status: Mapped[str] = mapped_column(String(16), nullable=False)
    rows_total: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    rows_imported: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    errors: Mapped[list] = mapped_column(json_document, nullable=False, default=list)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    connection: Mapped[DataSourceConnection] = relationship(back_populates="runs")
    mapping: Mapped[DataSourceMapping] = relationship()
    actor: Mapped["User"] = relationship()
