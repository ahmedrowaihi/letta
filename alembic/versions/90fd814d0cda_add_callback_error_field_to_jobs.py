"""Add callback error field to jobs

Revision ID: 90fd814d0cda
Revises: c0ef3ff26306
Create Date: 2025-06-16 13:04:53.496195

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "90fd814d0cda"
down_revision: Union[str, None] = "c0ef3ff26306"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("jobs", sa.Column("callback_error", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("jobs", "callback_error")
    # ### end Alembic commands ###
