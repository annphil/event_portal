"""posts table with date time

Revision ID: 284b6c138008
Revises: c104ddef0e7c
Create Date: 2021-05-23 17:36:43.001768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '284b6c138008'
down_revision = 'c104ddef0e7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('name', sa.String(length=140), nullable=True))
    op.add_column('post', sa.Column('host', sa.String(length=140), nullable=True))
    op.add_column('post', sa.Column('date', sa.String(length=140), nullable=True))
    op.add_column('post', sa.Column('time', sa.String(length=140), nullable=True))
    op.drop_column('post', 'body')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body', sa.VARCHAR(length=140), nullable=True))
    op.drop_column('post', 'time')
    op.drop_column('post', 'date')
    op.drop_column('post', 'host')
    op.drop_column('post', 'name')
    # ### end Alembic commands ###
