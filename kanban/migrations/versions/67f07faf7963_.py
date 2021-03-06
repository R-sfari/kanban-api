"""empty message

Revision ID: 67f07faf7963
Revises: 9fe4a364d342
Create Date: 2020-01-24 12:32:59.547044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67f07faf7963'
down_revision = '9fe4a364d342'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('analytics',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('event', sa.Text(), nullable=True),
    sa.Column('data', sa.PickleType(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analytics')
    # ### end Alembic commands ###
