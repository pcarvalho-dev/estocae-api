"""empty message

Revision ID: 950993a55953
Revises: 51a90d0d469e
Create Date: 2024-03-20 18:30:01.570091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '950993a55953'
down_revision = '51a90d0d469e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coupon', sa.Column('product_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'coupon', 'product', ['product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'coupon', type_='foreignkey')
    op.drop_column('coupon', 'product_id')
    # ### end Alembic commands ###
