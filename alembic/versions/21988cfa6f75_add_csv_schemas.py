"""Add CSV Schemas

Revision ID: 21988cfa6f75
Revises: edd7607cffd1
Create Date: 2020-03-02 17:56:46.523154

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '21988cfa6f75'
down_revision = 'edd7607cffd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'transaction_field_mappings', ['id'])
    op.create_unique_constraint(None, 'transaction_fields', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'transaction_fields', type_='unique')
    op.drop_constraint(None, 'transaction_field_mappings', type_='unique')
    # ### end Alembic commands ###
