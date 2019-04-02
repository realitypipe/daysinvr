"""empty message

Revision ID: 37f460a1f4d2
Revises: 1584139036cb
Create Date: 2019-02-28 14:53:48.334389

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB


# revision identifiers, used by Alembic.
revision = '37f460a1f4d2'
down_revision = '1584139036cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=50), nullable=True),
    sa.Column('uri', sa.String(length=512), nullable=True),
    sa.Column('filemime', sa.String(length=255), nullable=True),
    sa.Column('filesize', sa.Integer(), nullable=True),
    sa.Column('filename_original', sa.String(length=200), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('theme',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=False),
    sa.Column('config', JSONB(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['userprofile.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('title')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('slug', sa.String(length=100), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=False),
    sa.Column('theme_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['userprofile.id'], ),
    sa.ForeignKeyConstraint(['theme_id'], ['theme.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(length=100), nullable=True),
    sa.Column('type', sa.String(length=50), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['parent_id'], ['field.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['author_id'], ['userprofile.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('audio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('audio_format', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('number',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('photosphere',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('x', sa.Numeric(), nullable=True),
    sa.Column('y', sa.Numeric(), nullable=True),
    sa.Column('z', sa.Numeric(), nullable=True),
    sa.Column('w', sa.Numeric(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('video',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('videosphere',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_id', sa.Integer(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('width', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['file_id'], ['file.id'], ),
    sa.ForeignKeyConstraint(['id'], ['field.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tagname', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritor_assoc',
    sa.Column('favoriter', sa.Integer(), nullable=True),
    sa.Column('favorited_project', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['favorited_project'], ['project.id'], ),
    sa.ForeignKeyConstraint(['favoriter'], ['userprofile.id'], )
    )
    op.create_table('tag_assoc',
    sa.Column('tag', sa.Integer(), nullable=True),
    sa.Column('project', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project'], ['project.id'], ),
    sa.ForeignKeyConstraint(['tag'], ['tags.id'], )
    )
    op.drop_table('projects')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('project_name', sa.VARCHAR(length=80), nullable=False),
    sa.Column('created_by', sa.INTEGER(), nullable=False),
    sa.Column('parent_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['userprofile.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('project_name')
    )
    op.add_column('tag_assoc', sa.Column('article', sa.INTEGER(), nullable=True))
    op.drop_table('videosphere')
    op.drop_table('video')
    op.drop_table('text')
    op.drop_table('position')
    op.drop_table('photosphere')
    op.drop_table('number')
    op.drop_table('image')
    op.drop_table('audio')
    op.drop_table('field')
    op.drop_table('theme')
    op.drop_table('file')
    op.drop_table('tags')
    op.drop_table('tag_assoc')
    op.drop_table('favoritor_assoc')
    op.drop_table('project')
    # ### end Alembic commands ###
