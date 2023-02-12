"""add content column to posts table

Revision ID: 2149e53820fe
Revises: 4ee24d28cfed
Create Date: 2023-02-10 21:25:57.545351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2149e53820fe'
down_revision = '4ee24d28cfed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
    sa.Column('content', sa.String, nullable=False))


def downgrade() -> None:
    op.drop_column('posts', 'content')
