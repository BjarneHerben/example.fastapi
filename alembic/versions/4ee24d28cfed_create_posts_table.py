"""create_posts_table

Revision ID: 4ee24d28cfed
Revises: 
Create Date: 2023-02-10 21:14:32.673527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ee24d28cfed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
    sa.Column('id', sa.Integer, nullable=False, primary_key=True),
    sa.Column('title', sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('posts')
