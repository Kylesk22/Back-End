"""empty message

Revision ID: c6a4fa5518f3
Revises: 
Create Date: 2022-10-20 03:25:34.978536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6a4fa5518f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gym',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gym_name', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('gym_name')
    )
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gym_id', sa.Integer(), nullable=True),
    sa.Column('event_name', sa.String(length=80), nullable=False),
    sa.Column('event_date', sa.Integer(), nullable=False),
    sa.Column('event_description', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['gym_id'], ['gym.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=False),
    sa.Column('last_name', sa.String(length=80), nullable=False),
    sa.Column('gym_id', sa.Integer(), nullable=True),
    sa.Column('friends', sa.String(length=80), nullable=True),
    sa.Column('pending_friend_requests', sa.String(length=80), nullable=True),
    sa.Column('sent_friend_requests', sa.String(length=80), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['gym_id'], ['gym.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('event_posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('event_post_data', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posting',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_info', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posting')
    op.drop_table('event_posts')
    op.drop_table('user')
    op.drop_table('event')
    op.drop_table('gym')
    # ### end Alembic commands ###
