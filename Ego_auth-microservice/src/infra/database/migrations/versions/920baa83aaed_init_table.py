"""init table

Revision ID: 920baa83aaed
Revises:
Create Date: 2023-06-15 12:53:11.223613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '920baa83aaed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('salt', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('user_email', sa.String(), nullable=False),
    sa.Column(
        'time_created',
        sa.DateTime(),
        server_default=sa.text('now()'),
        nullable=False
    ),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
