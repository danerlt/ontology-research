"""新增本体分支与资源级评审

Revision ID: c9d47115bd48
Revises: 2a828f2b5f3b
Create Date: 2026-11-15 08:52:58.069733

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = 'c9d47115bd48'
down_revision: Union[str, Sequence[str], None] = '2a828f2b5f3b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    json_document = sa.JSON().with_variant(postgresql.JSONB(astext_type=sa.Text()), "postgresql")
    op.create_table(
        "ontology_branches",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("ontology_id", sa.Uuid(), nullable=False),
        sa.Column("author_id", sa.Uuid(), nullable=False),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("description", sa.String(length=2000), nullable=False),
        sa.Column("base_revision", sa.Integer(), nullable=False),
        sa.Column("base_snapshot", json_document, nullable=False),
        sa.Column("snapshot", json_document, nullable=False),
        sa.Column("changes", json_document, nullable=False),
        sa.Column("validation", json_document, nullable=False),
        sa.Column("status", sa.String(length=16), server_default="active", nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint(
            "status IN ('active', 'proposed', 'merged', 'closed')", name="ck_ontology_branches_status"
        ),
        sa.ForeignKeyConstraint(["author_id"], ["users.id"], ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["ontology_id"], ["ontologies.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("ontology_id", "name", name="uq_ontology_branches_ontology_name"),
    )
    op.create_index(op.f("ix_ontology_branches_author_id"), "ontology_branches", ["author_id"], unique=False)
    op.create_index(op.f("ix_ontology_branches_ontology_id"), "ontology_branches", ["ontology_id"], unique=False)
    op.add_column("change_proposals", sa.Column("branch_id", sa.Uuid(), nullable=True))
    op.create_index(op.f("ix_change_proposals_branch_id"), "change_proposals", ["branch_id"], unique=False)
    op.create_foreign_key(
        "fk_change_proposals_branch_id_ontology_branches",
        "change_proposals",
        "ontology_branches",
        ["branch_id"],
        ["id"],
        ondelete="SET NULL",
    )
    op.create_table(
        "proposal_resource_reviews",
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("proposal_id", sa.Uuid(), nullable=False),
        sa.Column("resource_key", sa.String(length=200), nullable=False),
        sa.Column("status", sa.String(length=16), server_default="pending", nullable=False),
        sa.Column("reviewer_id", sa.Uuid(), nullable=True),
        sa.Column("comment", sa.String(length=2000), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.CheckConstraint("status IN ('pending', 'approved', 'rejected')", name="ck_proposal_resource_reviews_status"),
        sa.ForeignKeyConstraint(["proposal_id"], ["change_proposals.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["reviewer_id"], ["users.id"], ondelete="SET NULL"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("proposal_id", "resource_key", name="uq_proposal_resource_reviews_key"),
    )
    op.create_index(
        op.f("ix_proposal_resource_reviews_proposal_id"), "proposal_resource_reviews", ["proposal_id"], unique=False
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_proposal_resource_reviews_proposal_id"), table_name="proposal_resource_reviews")
    op.drop_table("proposal_resource_reviews")
    op.drop_constraint("fk_change_proposals_branch_id_ontology_branches", "change_proposals", type_="foreignkey")
    op.drop_index(op.f("ix_change_proposals_branch_id"), table_name="change_proposals")
    op.drop_column("change_proposals", "branch_id")
    op.drop_index(op.f("ix_ontology_branches_ontology_id"), table_name="ontology_branches")
    op.drop_index(op.f("ix_ontology_branches_author_id"), table_name="ontology_branches")
    op.drop_table("ontology_branches")
