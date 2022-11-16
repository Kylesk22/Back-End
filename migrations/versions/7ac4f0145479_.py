"""empty message

Revision ID: 7ac4f0145479
Revises: 020416fc92f4
Create Date: 2022-11-16 10:21:55.572302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ac4f0145479'
down_revision = '020416fc92f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_gym',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('gym_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gym_id'], ['gym.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.add_column('gym', sa.Column('name', sa.String(length=30), nullable=False))
    op.drop_constraint('gym_gym_name_key', 'gym', type_='unique')
    op.create_unique_constraint(None, 'gym', ['name'])
    op.drop_column('gym', 'gym_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gym', sa.Column('gym_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'gym', type_='unique')
    op.create_unique_constraint('gym_gym_name_key', 'gym', ['gym_name'])
    op.drop_column('gym', 'name')
    op.drop_table('user_gym')
    # ### end Alembic commands ###