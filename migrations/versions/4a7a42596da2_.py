"""empty message

Revision ID: 4a7a42596da2
Revises: af23a6ccf698
Create Date: 2020-04-18 06:03:12.704709

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a7a42596da2'
down_revision = 'af23a6ccf698'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('deleted', sa.Boolean(), nullable=True))
    op.add_column('vehicle', sa.Column('deleted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vehicle', 'deleted')
    op.drop_column('user', 'deleted')
    # ### end Alembic commands ###
