from collections.abc import Generator

from sqlalchemy import and_, create_engine, event
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker, with_loader_criteria

from backend.ontology_service.app.config import get_settings


class Base(DeclarativeBase):
    pass


engine = create_engine(get_settings().database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session


@event.listens_for(Session, "do_orm_execute")
def apply_project_scope(execute_state) -> None:
    project_id = execute_state.session.info.get("project_id")
    if project_id is None or not (
        execute_state.is_select or execute_state.is_update or execute_state.is_delete
    ):
        return

    from backend.ontology_service.app.models import (
        ActionDefinition,
        AgentDefinition,
        AgentEvent,
        AgentSession,
        AgentVersion,
        AuditEvent,
        ChangeProposal,
        DataImportRun,
        DataSourceConnection,
        DataSourceMapping,
        LinkType,
        ObjectLink,
        ObjectRecord,
        ObjectType,
        Ontology,
        OntologyBranch,
        PropertyDefinition,
        ProposalResourceReview,
    )

    criteria = (
        with_loader_criteria(
            Ontology,
            lambda model: model.project_id == project_id,
            include_aliases=True,
        ),
        with_loader_criteria(
            ObjectType,
            lambda model: model.ontology.has(Ontology.project_id == project_id),
            include_aliases=True,
        ),
        with_loader_criteria(
            PropertyDefinition,
            lambda model: model.object_type.has(ObjectType.ontology.has(Ontology.project_id == project_id)),
            include_aliases=True,
        ),
        with_loader_criteria(
            LinkType,
            lambda model: model.ontology.has(Ontology.project_id == project_id),
            include_aliases=True,
        ),
        with_loader_criteria(
            ObjectRecord,
            lambda model: model.object_type.has(ObjectType.ontology.has(Ontology.project_id == project_id)),
            include_aliases=True,
        ),
        with_loader_criteria(
            ObjectLink,
            lambda model: and_(
                model.link_type.has(LinkType.ontology.has(Ontology.project_id == project_id)),
                model.source_object.has(ObjectRecord.object_type.has(ObjectType.ontology.has(Ontology.project_id == project_id))),
                model.target_object.has(ObjectRecord.object_type.has(ObjectType.ontology.has(Ontology.project_id == project_id))),
            ),
            include_aliases=True,
        ),
        with_loader_criteria(
            ActionDefinition,
            lambda model: model.object_type.has(ObjectType.ontology.has(Ontology.project_id == project_id)),
            include_aliases=True,
        ),
        with_loader_criteria(
            ChangeProposal,
            lambda model: model.ontology.has(Ontology.project_id == project_id),
            include_aliases=True,
        ),
        with_loader_criteria(
            OntologyBranch,
            lambda model: model.ontology.has(Ontology.project_id == project_id),
            include_aliases=True,
        ),
        with_loader_criteria(
            ProposalResourceReview,
            lambda model: model.proposal.has(ChangeProposal.ontology.has(Ontology.project_id == project_id)),
            include_aliases=True,
        ),
        with_loader_criteria(
            DataSourceConnection,
            lambda model: model.ontology.has(Ontology.project_id == project_id),
            include_aliases=True,
        ),
        with_loader_criteria(
            DataSourceMapping,
            lambda model: and_(
                model.connection.has(DataSourceConnection.ontology.has(Ontology.project_id == project_id)),
                model.object_type.has(ObjectType.ontology.has(Ontology.project_id == project_id)),
            ),
            include_aliases=True,
        ),
        with_loader_criteria(
            DataImportRun,
            lambda model: model.connection.has(DataSourceConnection.ontology.has(Ontology.project_id == project_id)),
            include_aliases=True,
        ),
        with_loader_criteria(
            AgentDefinition,
            lambda model: model.project_id == project_id,
            include_aliases=True,
        ),
        with_loader_criteria(
            AgentVersion,
            lambda model: model.agent.has(AgentDefinition.project_id == project_id),
            include_aliases=True,
        ),
        with_loader_criteria(
            AgentSession,
            lambda model: model.agent.has(AgentDefinition.project_id == project_id),
            include_aliases=True,
        ),
        with_loader_criteria(
            AgentEvent,
            lambda model: model.session.has(AgentSession.agent.has(AgentDefinition.project_id == project_id)),
            include_aliases=True,
        ),
        with_loader_criteria(
            AuditEvent,
            lambda model: model.project_id == project_id,
            include_aliases=True,
        ),
    )
    execute_state.statement = execute_state.statement.options(*criteria)
