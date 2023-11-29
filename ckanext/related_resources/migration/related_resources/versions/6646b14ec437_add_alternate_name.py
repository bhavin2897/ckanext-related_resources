"""add alternate name

Revision ID: 6646b14ec437
Revises: b12b6c615fc7
Create Date: 2022-02-11 09:09:48.146170

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6646b14ec437'
down_revision = 'b12b6c615fc7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('related_resources', sa.Column('alternate_name', sa.UnicodeText, nullable=True))


def downgrade():
    op.drop_column('related_resources', 'alternateName')
