"""empty message

Revision ID: 5933fa093e9e
Revises: 
Create Date: 2024-09-29 12:00:19.873878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5933fa093e9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('reptile_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    # ### end Alembic commands ###
