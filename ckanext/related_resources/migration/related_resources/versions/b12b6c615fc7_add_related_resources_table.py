"""Add related resources table

Revision ID: b12b6c615fc7
Revises: 
Create Date: 2022-01-31 09:47:04.843215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b12b6c615fc7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('related_resources',
                    sa.Column('id', sa.Integer, primary_key=True, nullable=False),
                    sa.Column('package_id', sa.UnicodeText(), sa.ForeignKey('package.id'), nullable=False),
                    sa.Column('relation_id', sa.UnicodeText()),
                    sa.Column('relationType', sa.UnicodeText()),
                    sa.Column('relationIdType', sa.UnicodeText())
                    )

def downgrade():
    op.drop_table('related_resources')
