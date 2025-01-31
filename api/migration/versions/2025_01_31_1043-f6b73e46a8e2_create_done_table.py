"""create done table

Revision ID: f6b73e46a8e2
Revises: 89da12e3bc26
Create Date: 2025-01-31 10:43:06.241077+09:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6b73e46a8e2'
down_revision: Union[str, None] = '89da12e3bc26'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
