"""empty message

Revision ID: 15e823d829bd
Revises: 
Create Date: 2017-10-24 19:02:20.523418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15e823d829bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('credit_card', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('driver', sa.Boolean(), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=25), nullable=False),
    sa.Column('date_created', sa.String(length=50), nullable=True),
    sa.Column('date_modified', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('drives',
    sa.Column('ride_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.Column('start_location', sa.String(length=50), nullable=False),
    sa.Column('end_location', sa.String(length=50), nullable=False),
    sa.Column('time_finished', sa.String(length=50), nullable=True),
    sa.Column('picked_up', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['users.user_id'], ),
    sa.ForeignKeyConstraint(['driver_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('ride_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drives')
    op.drop_table('users')
    # ### end Alembic commands ###
