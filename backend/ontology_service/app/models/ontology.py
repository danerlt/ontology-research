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


class Ontology(Base):
    __tablename__ = "ontologies"

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    api_name: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    display_name: Mapped[str] = mapped_column(String(160), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    revision: Mapped[int] = mapped_column(Integer, nullable=False, default=1, server_default="1")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now()
    )

    object_types: Mapped[list["ObjectType"]] = relationship(
        back_populates="ontology", cascade="all, delete-orphan"
    )
    link_types: Mapped[list["LinkType"]] = relationship(
        back_populates="ontology", cascade="all, delete-orphan"
    )


class ObjectType(Base):
    __tablename__ = "object_types"
    __table_args__ = (
        UniqueConstraint("ontology_id", "api_name", name="uq_object_types_ontology_api_name"),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    ontology_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("ontologies.id", ondelete="CASCADE"), nullable=False, index=True
    )
    api_name: Mapped[str] = mapped_column(String(80), nullable=False)
    display_name: Mapped[str] = mapped_column(String(160), nullable=False)
    plural_display_name: Mapped[str] = mapped_column(String(160), default="", server_default="", nullable=False)
    description: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    primary_key_property: Mapped[str] = mapped_column(String(80), default="id", nullable=False)
    title_key_property: Mapped[str] = mapped_column(String(80), default="id", server_default="id", nullable=False)
    aliases: Mapped[list[str]] = mapped_column(json_document, default=list, server_default="[]", nullable=False)
    groups: Mapped[list[str]] = mapped_column(json_document, default=list, server_default="[]", nullable=False)
    icon: Mapped[str] = mapped_column(String(64), default="object", server_default="object", nullable=False)
    icon_color: Mapped[str] = mapped_column(String(16), default="#4F8067", server_default="#4F8067", nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    ontology: Mapped[Ontology] = relationship(back_populates="object_types")
    properties: Mapped[list["PropertyDefinition"]] = relationship(
        back_populates="object_type", cascade="all, delete-orphan"
    )


class PropertyDefinition(Base):
    __tablename__ = "property_definitions"
    __table_args__ = (
        UniqueConstraint("object_type_id", "api_name", name="uq_properties_type_api_name"),
        CheckConstraint(
            "data_type IN ('string', 'integer', 'number', 'boolean', 'date', 'datetime', 'enum', 'json')",
            name="ck_properties_data_type",
        ),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    object_type_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("object_types.id", ondelete="CASCADE"), nullable=False, index=True
    )
    api_name: Mapped[str] = mapped_column(String(80), nullable=False)
    display_name: Mapped[str] = mapped_column(String(160), nullable=False)
    data_type: Mapped[str] = mapped_column(String(16), nullable=False)
    required: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default="false")
    editable: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")
    unique_value: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default="false")
    sensitive: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default="false")
    options: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict, server_default="{}")

    object_type: Mapped[ObjectType] = relationship(back_populates="properties")


class LinkType(Base):
    __tablename__ = "link_types"
    __table_args__ = (
        UniqueConstraint("ontology_id", "api_name", name="uq_link_types_ontology_api_name"),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    ontology_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("ontologies.id", ondelete="CASCADE"), nullable=False, index=True
    )
    api_name: Mapped[str] = mapped_column(String(80), nullable=False)
    display_name: Mapped[str] = mapped_column(String(160), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    source_type_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("object_types.id", ondelete="CASCADE"), nullable=False, index=True
    )
    target_type_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("object_types.id", ondelete="CASCADE"), nullable=False, index=True
    )
    ontology: Mapped[Ontology] = relationship(back_populates="link_types")
    source_type: Mapped[ObjectType] = relationship(foreign_keys=[source_type_id])
    target_type: Mapped[ObjectType] = relationship(foreign_keys=[target_type_id])
