"""扩展Action参数校验与提交条件

Revision ID: e6c1bdb45e54
Revises: c9d47115bd48
Create Date: 2026-11-15 09:06:44.058541

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'e6c1bdb45e54'
down_revision: Union[str, Sequence[str], None] = 'c9d47115bd48'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    json_document = sa.JSON().with_variant(postgresql.JSONB(astext_type=sa.Text()), "postgresql")
    op.add_column(
        "action_definitions",
        sa.Column("submission_criteria", json_document, server_default="{}", nullable=False),
    )
    op.alter_column("action_definitions", "submission_criteria", server_default=None)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("action_definitions", "submission_criteria")
