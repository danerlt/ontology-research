"""扩展对象类型元数据

Revision ID: 2524472d984a
Revises: 99d0561ebd52
Create Date: 2026-11-15 10:52:18.547830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '2524472d984a'
down_revision: Union[str, Sequence[str], None] = '99d0561ebd52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """扩展对象类型的展示与检索元数据。"""
    json_list = sa.JSON().with_variant(postgresql.JSONB(astext_type=sa.Text()), "postgresql")
    op.add_column("object_types", sa.Column("plural_display_name", sa.String(length=160), nullable=True))
    op.add_column("object_types", sa.Column("title_key_property", sa.String(length=80), nullable=True))
    op.add_column("object_types", sa.Column("aliases", json_list, nullable=True))
    op.add_column("object_types", sa.Column("groups", json_list, nullable=True))
    op.add_column("object_types", sa.Column("icon", sa.String(length=64), nullable=True))
    op.add_column("object_types", sa.Column("icon_color", sa.String(length=16), nullable=True))

    op.execute(sa.text("UPDATE object_types SET plural_display_name = display_name WHERE plural_display_name IS NULL"))
    op.execute(sa.text("UPDATE object_types SET title_key_property = primary_key_property WHERE title_key_property IS NULL"))
    op.execute(sa.text("""
        UPDATE object_types
        SET title_key_property = 'name'
        WHERE EXISTS (
            SELECT 1 FROM property_definitions
            WHERE property_definitions.object_type_id = object_types.id
              AND property_definitions.api_name = 'name'
        )
    """))
    op.execute(sa.text("UPDATE object_types SET aliases = '[]', groups = '[]', icon = 'object', icon_color = '#4F8067'"))

    op.alter_column("object_types", "plural_display_name", existing_type=sa.String(length=160), nullable=False, server_default="")
    op.alter_column("object_types", "title_key_property", existing_type=sa.String(length=80), nullable=False, server_default="id")
    op.alter_column("object_types", "aliases", existing_type=json_list, nullable=False, server_default=sa.text("'[]'"))
    op.alter_column("object_types", "groups", existing_type=json_list, nullable=False, server_default=sa.text("'[]'"))
    op.alter_column("object_types", "icon", existing_type=sa.String(length=64), nullable=False, server_default="object")
    op.alter_column("object_types", "icon_color", existing_type=sa.String(length=16), nullable=False, server_default="#4F8067")


def downgrade() -> None:
    """移除新增的对象类型元数据。"""
    op.drop_column("object_types", "icon_color")
    op.drop_column("object_types", "icon")
    op.drop_column("object_types", "groups")
    op.drop_column("object_types", "aliases")
    op.drop_column("object_types", "title_key_property")
    op.drop_column("object_types", "plural_display_name")
