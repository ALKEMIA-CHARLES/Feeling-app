"""second  migrate

Revision ID: 64e8fdcac022
Revises: 
Create Date: 2019-12-03 15:09:08.068778

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64e8fdcac022'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('affirmations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('database_affirmations_title', sa.String(), nullable=True),
    sa.Column('database_affirmations_post_section', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('useraffirmations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_affirmations_title', sa.String(), nullable=True),
    sa.Column('user_affirmations_post_section', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comments_section', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('database_affirmations_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['database_affirmations_id'], ['affirmations.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('useraffirmations')
    op.drop_table('affirmations')
    op.drop_table('users')
    # ### end Alembic commands ###
