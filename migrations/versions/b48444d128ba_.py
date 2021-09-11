"""empty message

Revision ID: b48444d128ba
Revises: 3847e6d3718b
Create Date: 2021-09-11 00:00:43.763487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b48444d128ba'
down_revision = '3847e6d3718b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employer', sa.Column('profile_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'employer', 'profile', ['profile_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'employer', type_='foreignkey')
    op.drop_column('employer', 'profile_id')
    # ### end Alembic commands ###
