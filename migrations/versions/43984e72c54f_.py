"""empty message

Revision ID: 43984e72c54f
Revises: 50cdb0220f90
Create Date: 2024-01-30 23:07:17.272070

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '43984e72c54f'
down_revision = '50cdb0220f90'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('hash_id', sa.String(length=36), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', mysql.LONGTEXT(collation='utf8mb4_bin'), nullable=True),
    sa.Column('sales_link', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.add_column('user', sa.Column('document', sa.String(length=255), nullable=True))
    op.drop_column('user', 'taxpayer')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('taxpayer', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('user', 'document')
    op.drop_table('product')
    # ### end Alembic commands ###
