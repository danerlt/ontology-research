"""添加链接基数

Revision ID: 8ef7708b3491
Revises: ecfe6abac4d7
Create Date: 2026-11-15 19:25:59.408450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ef7708b3491'
down_revision: Union[str, Sequence[str], None] = 'ecfe6abac4d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "link_types",
        sa.Column("source_cardinality", sa.String(length=8), server_default="many", nullable=False),
    )
    op.add_column(
        "link_types",
        sa.Column("target_cardinality", sa.String(length=8), server_default="many", nullable=False),
    )
    op.create_check_constraint("ck_links_source_cardinality", "link_types", "source_cardinality IN ('one', 'many')")
    op.create_check_constraint("ck_links_target_cardinality", "link_types", "target_cardinality IN ('one', 'many')")


def downgrade() -> None:
    op.drop_constraint("ck_links_target_cardinality", "link_types", type_="check")
    op.drop_constraint("ck_links_source_cardinality", "link_types", type_="check")
    op.drop_column("link_types", "target_cardinality")
    op.drop_column("link_types", "source_cardinality")
