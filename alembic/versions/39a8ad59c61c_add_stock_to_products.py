"""add stock to products

Revision ID: 39a8ad59c61c
Revises: 248ad4a2dc62
Create Date: 2026-06-06 16:26:31.614013
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '39a8ad59c61c'
down_revision: Union[str, Sequence[str], None] = '248ad4a2dc62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'products',
        sa.Column(
            'stock',
            sa.Integer(),
            nullable=False,
            server_default='0'
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('products', 'stock')