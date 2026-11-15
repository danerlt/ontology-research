"""新增 Agent 配置与发布版本

Revision ID: 99d0561ebd52
Revises: 2b1ddd86e785
Create Date: 2026-11-15 09:58:13.564049

"""
from typing import Sequence, Union
from uuid import uuid4

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '99d0561ebd52'
down_revision: Union[str, Sequence[str], None] = '2b1ddd86e785'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """保存 Agent 草稿快照，并让会话固定到不可变发布版本。"""
    json_document = sa.JSON().with_variant(postgresql.JSONB(astext_type=sa.Text()), "postgresql")
    op.add_column("agent_definitions", sa.Column("draft_config", json_document, nullable=True))
    op.create_table(
        "agent_versions",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("agent_id", sa.Uuid(), nullable=False),
        sa.Column("version_number", sa.Integer(), nullable=False),
        sa.Column("config", json_document, nullable=False),
        sa.Column("created_by", sa.Uuid(), nullable=True),
        sa.Column("published_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["agent_id"], ["agent_definitions.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["created_by"], ["users.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("agent_id", "version_number", name="uq_agent_versions_agent_number"),
    )
    op.create_index("ix_agent_versions_agent_id", "agent_versions", ["agent_id"])
    op.add_column("agent_sessions", sa.Column("agent_version_id", sa.Uuid(), nullable=True))
    op.add_column("agent_sessions", sa.Column("input_values", json_document, nullable=True))
    op.add_column(
        "agent_sessions",
        sa.Column("origin_resource", sa.String(length=255), server_default="local-workbench", nullable=False),
    )

    connection = op.get_bind()
    agent_table = sa.table(
        "agent_definitions",
        sa.column("id", sa.Uuid()),
        sa.column("api_name", sa.String()),
        sa.column("display_name", sa.String()),
        sa.column("description", sa.String()),
        sa.column("allowed_tools", json_document),
        sa.column("allowed_actions", json_document),
        sa.column("draft_config", json_document),
    )
    version_table = sa.table(
        "agent_versions",
        sa.column("id", sa.Uuid()),
        sa.column("agent_id", sa.Uuid()),
        sa.column("version_number", sa.Integer()),
        sa.column("config", json_document),
    )
    session_table = sa.table(
        "agent_sessions",
        sa.column("agent_id", sa.Uuid()),
        sa.column("agent_version_id", sa.Uuid()),
        sa.column("input_values", json_document),
    )
    agents = connection.execute(
        sa.select(
            agent_table.c.id,
            agent_table.c.api_name,
            agent_table.c.display_name,
            agent_table.c.description,
            agent_table.c.allowed_tools,
            agent_table.c.allowed_actions,
        )
    ).mappings()
    for agent in agents:
        config = {
            "model_provider": "local",
            "model_name": "确定性本地预览",
            "system_prompt": agent["description"] or f"你是{agent['display_name']}。",
            "initial_user_message": "",
            "inputs": [],
            "precomputed_variables": [],
            "allowed_tools": agent["allowed_tools"] or [],
            "allowed_actions": agent["allowed_actions"] or [],
            "session_completion": {"mode": "stays_open", "output_schema": {}},
        }
        version_id = uuid4()
        connection.execute(
            agent_table.update().where(agent_table.c.id == agent["id"]).values(draft_config=config)
        )
        connection.execute(
            version_table.insert().values(
                id=version_id,
                agent_id=agent["id"],
                version_number=1,
                config=config,
            )
        )
        connection.execute(
            session_table.update()
            .where(session_table.c.agent_id == agent["id"])
            .values(agent_version_id=version_id)
        )

    op.execute(sa.text("UPDATE agent_sessions SET input_values = '{}' WHERE input_values IS NULL"))
    op.alter_column("agent_definitions", "draft_config", existing_type=json_document, nullable=False)
    op.alter_column("agent_sessions", "agent_version_id", existing_type=sa.Uuid(), nullable=False)
    op.alter_column("agent_sessions", "input_values", existing_type=json_document, nullable=False)
    op.create_index("ix_agent_sessions_agent_version_id", "agent_sessions", ["agent_version_id"])
    op.create_foreign_key(
        "fk_agent_sessions_agent_version_id_agent_versions",
        "agent_sessions",
        "agent_versions",
        ["agent_version_id"],
        ["id"],
        ondelete="RESTRICT",
    )


def downgrade() -> None:
    """移除 Agent 发布版本、草稿配置和会话快照字段。"""
    op.drop_constraint(
        "fk_agent_sessions_agent_version_id_agent_versions", "agent_sessions", type_="foreignkey"
    )
    op.drop_index("ix_agent_sessions_agent_version_id", table_name="agent_sessions")
    op.drop_column("agent_sessions", "origin_resource")
    op.drop_column("agent_sessions", "input_values")
    op.drop_column("agent_sessions", "agent_version_id")
    op.drop_index("ix_agent_versions_agent_id", table_name="agent_versions")
    op.drop_table("agent_versions")
    op.drop_column("agent_definitions", "draft_config")
