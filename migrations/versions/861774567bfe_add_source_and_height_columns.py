"""Add source and height columns

Revision ID: 861774567bfe
Revises: bc5221749cb0
Create Date: 2021-10-30 13:45:16.962581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '861774567bfe'
down_revision = 'bc5221749cb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eda', sa.Column('text', sa.String(), nullable=True))
    op.add_column('eda', sa.Column('source', sa.String(), nullable=True))
    op.add_column('eda', sa.Column('height', sa.String(), nullable=True))
    op.drop_column('eda', 'text_block')
    op.drop_column('eda', 'iframes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eda', sa.Column('iframes', sa.VARCHAR(), nullable=False))
    op.add_column('eda', sa.Column('text_block', sa.VARCHAR(), nullable=False))
    op.drop_column('eda', 'height')
    op.drop_column('eda', 'source')
    op.drop_column('eda', 'text')
    # ### end Alembic commands ###