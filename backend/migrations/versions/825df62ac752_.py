"""empty message

Revision ID: 825df62ac752
Revises: ec600df7860f
Create Date: 2019-09-04 17:57:07.992195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '825df62ac752'
down_revision = 'ec600df7860f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('activity_name', sa.String(length=200), nullable=True))
    op.add_column('classroom', sa.Column('age_students', sa.String(length=100), nullable=True))
    op.add_column('classroom', sa.Column('subject', sa.String(length=100), nullable=True))
    op.add_column('school', sa.Column('type', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('school', 'type')
    op.drop_column('classroom', 'subject')
    op.drop_column('classroom', 'age_students')
    op.drop_column('activity', 'activity_name')
    # ### end Alembic commands ###