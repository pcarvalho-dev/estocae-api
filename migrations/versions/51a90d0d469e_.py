"""empty message

Revision ID: 51a90d0d469e
Revises: 8722f280eaff
Create Date: 2024-03-20 18:22:14.354292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51a90d0d469e'
down_revision = '8722f280eaff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('offer', sa.Column('product_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'offer', 'product', ['product_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'offer', type_='foreignkey')
    op.drop_column('offer', 'product_id')
    # ### end Alembic commands ###
