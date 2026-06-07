"""add order status

Revision ID: 673c55df51cf
Revises: bfdeb262d8d5
Create Date: 2026-06-07 17:06:40.284965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '673c55df51cf'
down_revision: Union[str, Sequence[str], None] = 'bfdeb262d8d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        'orders',
        sa.Column(
            'status',
            sa.String(),
            nullable=False,
            server_default='PENDING'
        )
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        'orders',
        'status'
    )