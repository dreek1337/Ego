"""create my_tables

Revision ID: ade66a311248
Revises:
Create Date: 2023-06-01 19:08:27.537623

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ade66a311248"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("user_id", sa.BigInteger(), autoincrement=False, nullable=False),
        sa.Column("first_name", sa.String(length=128), nullable=False),
        sa.Column("last_name", sa.String(length=128), nullable=False),
        sa.Column(
            "gender", sa.Enum("MALE", "FEMALE", name="gendervalue"), nullable=False
        ),
        sa.Column("birthday", sa.Date(), nullable=False),
        sa.Column("deleted", sa.Boolean(), nullable=False),
        sa.Column("time_updated", sa.DateTime(), nullable=False),
        sa.Column(
            "time_created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("user_id"),
    )
    op.create_table(
        "avatars",
        sa.Column("avatar_id", sa.Uuid(), autoincrement=False, nullable=False),
        sa.Column("avatar_type", sa.String(length=10), nullable=False),
        sa.Column("avatar_content", sa.LargeBinary(), nullable=True),
        sa.Column("avatar_user_id", sa.BigInteger(), nullable=False),
        sa.Column("time_updated", sa.DateTime(), nullable=False),
        sa.Column(
            "time_created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["avatar_user_id"],
            ["users.user_id"],
        ),
        sa.PrimaryKeyConstraint("avatar_id"),
    )
    op.create_table(
        "subscriptions",
        sa.Column("subscription_subscriber_id", sa.BigInteger(), nullable=False),
        sa.Column("subscription_id", sa.BigInteger(), nullable=False),
        sa.Column("subscriber_id", sa.BigInteger(), nullable=False),
        sa.Column(
            "time_created",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["subscriber_id"],
            ["users.user_id"],
        ),
        sa.ForeignKeyConstraint(
            ["subscription_id"],
            ["users.user_id"],
        ),
        sa.PrimaryKeyConstraint("subscription_subscriber_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("subscriptions")
    op.drop_table("avatars")
    op.drop_table("users")
    # ### end Alembic commands ###
