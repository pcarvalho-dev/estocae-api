"""uuid in all

Revision ID: 45eb50268570
Revises: 0eb2a78fb7da
Create Date: 2023-07-24 17:09:01.813813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45eb50268570'
down_revision = '0eb2a78fb7da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('city', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.add_column('community', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.add_column('country', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.add_column('group', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.add_column('main_company', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.add_column('main_company_address', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.add_column('main_settings', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.add_column('state', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.drop_index('hash_id', table_name='user')
    op.add_column('user_address', sa.Column('hash_id', sa.String(length=36), nullable=False))
    op.add_column('user_code_password', sa.Column('hash_id', sa.String(length=36), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_code_password', 'hash_id')
    op.drop_column('user_address', 'hash_id')
    op.create_index('hash_id', 'user', ['hash_id'], unique=False)
    op.drop_column('state', 'hash_id')
    op.drop_column('main_settings', 'hash_id')
    op.drop_column('main_company_address', 'hash_id')
    op.drop_column('main_company', 'hash_id')
    op.drop_column('group', 'hash_id')
    op.drop_column('country', 'hash_id')
    op.drop_column('community', 'hash_id')
    op.drop_column('city', 'hash_id')
    # ### end Alembic commands ###
