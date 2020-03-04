"""create category table

Revision ID: fe67361fa473
Revises: 
Create Date: 2020-02-28 11:59:01.705546

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy.dialects import postgresql
# revision identifiers, used by Alembic.
revision = 'fe67361fa473'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table('categories')
