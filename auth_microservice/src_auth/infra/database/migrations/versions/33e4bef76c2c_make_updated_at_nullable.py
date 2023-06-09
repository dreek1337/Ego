"""make updated_at nullable

Revision ID: 33e4bef76c2c
Revises: 920baa83aaed
Create Date: 2023-06-15 13:23:09.368806

"""
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "33e4bef76c2c"
down_revision = "920baa83aaed"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "updated_at", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "users", "updated_at", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    # ### end Alembic commands ###
