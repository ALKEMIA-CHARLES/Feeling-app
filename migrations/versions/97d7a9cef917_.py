"""empty message

Revision ID: 97d7a9cef917
Revises: a8b2e977f5f2
Create Date: 2019-12-06 10:47:13.016066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97d7a9cef917'
down_revision = 'a8b2e977f5f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('affirmations', sa.Column('images_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('affirmations', 'images_path')
    # ### end Alembic commands ###
