"""add user table

Revision ID: 9350d783015a
Revises: 2149e53820fe
Create Date: 2023-02-10 21:31:22.280822

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9350d783015a'
down_revision = '2149e53820fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id', sa.Integer, nullable=False),
    sa.Column('email', sa.String, nullable=False),
    sa.Column('password', sa.String, nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                server_default=sa.text('now()'), nullable=False),
                sa.PrimaryKeyConstraint('id'),
                sa.UniqueConstraint('email')
    )


def downgrade() -> None:
    op.drop_table('users')
