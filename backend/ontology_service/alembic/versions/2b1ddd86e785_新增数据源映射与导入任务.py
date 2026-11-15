"""新增数据源映射与导入任务

Revision ID: 2b1ddd86e785
Revises: e6c1bdb45e54
Create Date: 2026-11-15 09:27:42.301273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '2b1ddd86e785'
down_revision: Union[str, Sequence[str], None] = 'e6c1bdb45e54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """创建本地数据源连接、字段映射和导入运行记录。"""
    json_document = sa.JSON().with_variant(postgresql.JSONB(astext_type=sa.Text()), "postgresql")
    op.create_table(
        "data_source_connections",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("ontology_id", sa.Uuid(), nullable=False),
        sa.Column("created_by_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=160), nullable=False),
        sa.Column("description", sa.String(length=2000), nullable=False),
        sa.Column("connector_type", sa.String(length=24), nullable=False),
        sa.Column("status", sa.String(length=16), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["created_by_id"], ["users.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["ontology_id"], ["ontologies.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("ontology_id", "name", name="uq_data_sources_ontology_name"),
    )
    op.create_index("ix_data_source_connections_ontology_id", "data_source_connections", ["ontology_id"])
    op.create_index("ix_data_source_connections_created_by_id", "data_source_connections", ["created_by_id"])

    op.create_table(
        "data_source_mappings",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("connection_id", sa.Uuid(), nullable=False),
        sa.Column("object_type_id", sa.Uuid(), nullable=False),
        sa.Column("primary_key_field", sa.String(length=160), nullable=False),
        sa.Column("field_mappings", json_document, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.ForeignKeyConstraint(["connection_id"], ["data_source_connections.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["object_type_id"], ["object_types.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("connection_id", "object_type_id", name="uq_data_source_mappings_type"),
    )
    op.create_index("ix_data_source_mappings_connection_id", "data_source_mappings", ["connection_id"])
    op.create_index("ix_data_source_mappings_object_type_id", "data_source_mappings", ["object_type_id"])

    op.create_table(
        "data_import_runs",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("connection_id", sa.Uuid(), nullable=False),
        sa.Column("mapping_id", sa.Uuid(), nullable=False),
        sa.Column("actor_id", sa.Uuid(), nullable=False),
        sa.Column("status", sa.String(length=16), nullable=False),
        sa.Column("rows_total", sa.Integer(), nullable=False),
        sa.Column("rows_imported", sa.Integer(), nullable=False),
        sa.Column("errors", json_document, nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("completed_at", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["actor_id"], ["users.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["connection_id"], ["data_source_connections.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["mapping_id"], ["data_source_mappings.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_data_import_runs_actor_id", "data_import_runs", ["actor_id"])
    op.create_index("ix_data_import_runs_connection_id", "data_import_runs", ["connection_id"])
    op.create_index("ix_data_import_runs_mapping_id", "data_import_runs", ["mapping_id"])


def downgrade() -> None:
    """删除数据导入记录、映射和连接。"""
    op.drop_index("ix_data_import_runs_mapping_id", table_name="data_import_runs")
    op.drop_index("ix_data_import_runs_connection_id", table_name="data_import_runs")
    op.drop_index("ix_data_import_runs_actor_id", table_name="data_import_runs")
    op.drop_table("data_import_runs")
    op.drop_index("ix_data_source_mappings_object_type_id", table_name="data_source_mappings")
    op.drop_index("ix_data_source_mappings_connection_id", table_name="data_source_mappings")
    op.drop_table("data_source_mappings")
    op.drop_index("ix_data_source_connections_created_by_id", table_name="data_source_connections")
    op.drop_index("ix_data_source_connections_ontology_id", table_name="data_source_connections")
    op.drop_table("data_source_connections")
