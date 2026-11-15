"""新增项目与成员隔离

Revision ID: ecfe6abac4d7
Revises: 2524472d984a
Create Date: 2026-11-15 19:00:50.478929

"""
from typing import Sequence, Union
from uuid import uuid4

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ecfe6abac4d7'
down_revision: Union[str, Sequence[str], None] = '2524472d984a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "projects",
        sa.Column("id", sa.Uuid(as_uuid=True), nullable=False),
        sa.Column("api_name", sa.String(length=80), nullable=False),
        sa.Column("display_name", sa.String(length=160), nullable=False),
        sa.Column("description", sa.String(length=2000), nullable=False),
        sa.Column("created_by_id", sa.Uuid(as_uuid=True), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_projects_api_name", "projects", ["api_name"], unique=True)
    op.create_table(
        "project_memberships",
        sa.Column("id", sa.Uuid(as_uuid=True), nullable=False),
        sa.Column("project_id", sa.Uuid(as_uuid=True), nullable=False),
        sa.Column("user_id", sa.Uuid(as_uuid=True), nullable=False),
        sa.Column("role", sa.String(length=16), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.CheckConstraint("role IN ('admin', 'editor', 'viewer')", name="ck_project_memberships_role"),
        sa.ForeignKeyConstraint(["project_id"], ["projects.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("project_id", "user_id", name="uq_project_memberships_project_user"),
    )
    op.create_index("ix_project_memberships_project_id", "project_memberships", ["project_id"])
    op.create_index("ix_project_memberships_user_id", "project_memberships", ["user_id"])

    op.add_column("ontologies", sa.Column("project_id", sa.Uuid(as_uuid=True), nullable=True))
    op.add_column("agent_definitions", sa.Column("project_id", sa.Uuid(as_uuid=True), nullable=True))
    op.add_column("audit_events", sa.Column("project_id", sa.Uuid(as_uuid=True), nullable=True))

    connection = op.get_bind()
    default_project_id = uuid4()
    owner_id = connection.execute(
        sa.text("SELECT id FROM users WHERE role = 'admin' ORDER BY created_at LIMIT 1")
    ).scalar_one_or_none()
    connection.execute(
        sa.text(
            "INSERT INTO projects (id, api_name, display_name, description, created_by_id) "
            "VALUES (:id, 'operations', '运营知识图谱', '现有本体与运行资源的默认项目。', :owner_id)"
        ),
        {"id": default_project_id, "owner_id": owner_id},
    )
    connection.execute(
        sa.text("UPDATE ontologies SET project_id = :project_id WHERE project_id IS NULL"),
        {"project_id": default_project_id},
    )
    connection.execute(
        sa.text("UPDATE agent_definitions SET project_id = :project_id WHERE project_id IS NULL"),
        {"project_id": default_project_id},
    )
    connection.execute(
        sa.text("UPDATE audit_events SET project_id = :project_id WHERE project_id IS NULL"),
        {"project_id": default_project_id},
    )
    for user_id, role in connection.execute(sa.text("SELECT id, role FROM users")):
        connection.execute(
            sa.text(
                "INSERT INTO project_memberships (id, project_id, user_id, role) "
                "VALUES (:id, :project_id, :user_id, :role)"
            ),
            {"id": uuid4(), "project_id": default_project_id, "user_id": user_id, "role": role},
        )

    op.alter_column("ontologies", "project_id", existing_type=sa.Uuid(as_uuid=True), nullable=False)
    op.alter_column("agent_definitions", "project_id", existing_type=sa.Uuid(as_uuid=True), nullable=False)
    op.alter_column("audit_events", "project_id", existing_type=sa.Uuid(as_uuid=True), nullable=False)
    op.create_index("ix_ontologies_project_id", "ontologies", ["project_id"])
    op.drop_index("ix_ontologies_api_name", table_name="ontologies")
    op.create_index("ix_ontologies_api_name", "ontologies", ["api_name"], unique=False)
    op.create_unique_constraint(
        "uq_ontologies_project_api_name", "ontologies", ["project_id", "api_name"]
    )
    op.create_foreign_key(
        "fk_ontologies_project_id_projects", "ontologies", "projects", ["project_id"], ["id"], ondelete="CASCADE"
    )
    op.create_index("ix_agent_definitions_project_id", "agent_definitions", ["project_id"])
    op.create_foreign_key(
        "fk_agent_definitions_project_id_projects",
        "agent_definitions",
        "projects",
        ["project_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_index("ix_agent_definitions_api_name", table_name="agent_definitions")
    op.create_index("ix_agent_definitions_api_name", "agent_definitions", ["api_name"], unique=False)
    op.create_unique_constraint(
        "uq_agents_project_api_name", "agent_definitions", ["project_id", "api_name"]
    )
    op.create_index("ix_audit_events_project_id", "audit_events", ["project_id"])
    op.create_foreign_key(
        "fk_audit_events_project_id_projects", "audit_events", "projects", ["project_id"], ["id"], ondelete="CASCADE"
    )


def downgrade() -> None:
    op.drop_constraint("fk_audit_events_project_id_projects", "audit_events", type_="foreignkey")
    op.drop_index("ix_audit_events_project_id", table_name="audit_events")
    op.drop_column("audit_events", "project_id")
    op.drop_constraint("uq_agents_project_api_name", "agent_definitions", type_="unique")
    op.drop_index("ix_agent_definitions_api_name", table_name="agent_definitions")
    op.create_index("ix_agent_definitions_api_name", "agent_definitions", ["api_name"], unique=True)
    op.drop_constraint("fk_agent_definitions_project_id_projects", "agent_definitions", type_="foreignkey")
    op.drop_index("ix_agent_definitions_project_id", table_name="agent_definitions")
    op.drop_column("agent_definitions", "project_id")
    op.drop_constraint("fk_ontologies_project_id_projects", "ontologies", type_="foreignkey")
    op.drop_constraint("uq_ontologies_project_api_name", "ontologies", type_="unique")
    op.drop_index("ix_ontologies_api_name", table_name="ontologies")
    op.create_index("ix_ontologies_api_name", "ontologies", ["api_name"], unique=True)
    op.drop_index("ix_ontologies_project_id", table_name="ontologies")
    op.drop_column("ontologies", "project_id")
    op.drop_index("ix_project_memberships_user_id", table_name="project_memberships")
    op.drop_index("ix_project_memberships_project_id", table_name="project_memberships")
    op.drop_table("project_memberships")
    op.drop_index("ix_projects_api_name", table_name="projects")
    op.drop_table("projects")
