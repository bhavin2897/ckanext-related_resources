"""alter column name

Revision ID: 4f03da7e83dd
Revises: 6646b14ec437
Create Date: 2022-02-16 11:32:58.223120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f03da7e83dd'
down_revision = '6646b14ec437'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name = 'related_resources', column_name = 'relationType', new_column_name = 'relation_type')
    op.alter_column(table_name='related_resources', column_name='relationIdType', new_column_name='relation_id_type')


def downgrade():
    pass
