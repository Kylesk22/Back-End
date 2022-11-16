"""empty message

Revision ID: d9f4f4827441
Revises: c6a4fa5518f3
Create Date: 2022-11-04 20:40:35.914695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9f4f4827441'
down_revision = 'c6a4fa5518f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('monday', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('tuesday', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('wednesday', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('thursday', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('friday', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('saturday', sa.String(length=80), nullable=True))
    op.add_column('user', sa.Column('sunday', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'sunday')
    op.drop_column('user', 'saturday')
    op.drop_column('user', 'friday')
    op.drop_column('user', 'thursday')
    op.drop_column('user', 'wednesday')
    op.drop_column('user', 'tuesday')
    op.drop_column('user', 'monday')
    # ### end Alembic commands ###