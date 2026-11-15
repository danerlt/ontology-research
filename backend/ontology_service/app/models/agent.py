from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, UniqueConstraint, Uuid, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.ontology_service.app.database import Base

json_document = JSON().with_variant(JSONB(), "postgresql")


class AgentDefinition(Base):
    __tablename__ = "agent_definitions"
    __table_args__ = (UniqueConstraint("project_id", "api_name", name="uq_agents_project_api_name"),)

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    project_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True
    )
    api_name: Mapped[str] = mapped_column(String(80), index=True)
    display_name: Mapped[str] = mapped_column(String(160), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), default="", nullable=False)
    allowed_tools: Mapped[list[str]] = mapped_column(json_document, nullable=False, default=list)
    allowed_actions: Mapped[list[str]] = mapped_column(json_document, nullable=False, default=list)
    draft_config: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict)
    enabled: Mapped[bool] = mapped_column(default=True, nullable=False, server_default="true")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    sessions: Mapped[list["AgentSession"]] = relationship(back_populates="agent")
    versions: Mapped[list["AgentVersion"]] = relationship(
        back_populates="agent", order_by="AgentVersion.version_number"
    )


class AgentVersion(Base):
    __tablename__ = "agent_versions"
    __table_args__ = (
        UniqueConstraint("agent_id", "version_number", name="uq_agent_versions_agent_number"),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    agent_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("agent_definitions.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    version_number: Mapped[int] = mapped_column(Integer, nullable=False)
    config: Mapped[dict] = mapped_column(json_document, nullable=False)
    created_by: Mapped[UUID | None] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True
    )
    published_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    agent: Mapped[AgentDefinition] = relationship(back_populates="versions")
    sessions: Mapped[list["AgentSession"]] = relationship(back_populates="version")


class AgentSession(Base):
    __tablename__ = "agent_sessions"

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    agent_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("agent_definitions.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    agent_version_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("agent_versions.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    actor_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False, index=True
    )
    input_values: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict)
    origin_resource: Mapped[str] = mapped_column(
        String(255), nullable=False, default="local-workbench", server_default="local-workbench"
    )
    status: Mapped[str] = mapped_column(String(16), nullable=False, default="active", server_default="active")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    closed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    agent: Mapped[AgentDefinition] = relationship(back_populates="sessions")
    version: Mapped[AgentVersion] = relationship(back_populates="sessions")
    events: Mapped[list["AgentEvent"]] = relationship(
        back_populates="session", cascade="all, delete-orphan", order_by="AgentEvent.sequence"
    )


class AgentEvent(Base):
    __tablename__ = "agent_events"
    __table_args__ = (
        UniqueConstraint("session_id", "sequence", name="uq_agent_events_session_sequence"),
    )

    id: Mapped[UUID] = mapped_column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    session_id: Mapped[UUID] = mapped_column(
        Uuid(as_uuid=True), ForeignKey("agent_sessions.id", ondelete="CASCADE"), nullable=False, index=True
    )
    sequence: Mapped[int] = mapped_column(Integer, nullable=False)
    event_type: Mapped[str] = mapped_column(String(80), nullable=False)
    tool_name: Mapped[str | None] = mapped_column(String(80), nullable=True)
    status: Mapped[str] = mapped_column(String(24), nullable=False)
    details: Mapped[dict] = mapped_column(json_document, nullable=False, default=dict)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    session: Mapped[AgentSession] = relationship(back_populates="events")
