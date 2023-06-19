"""create index on avatar_user_id

Revision ID: 9b6ae67797c3
Revises: 2886fafea9d6
Create Date: 2023-06-04 18:34:21.982435

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '9b6ae67797c3'
down_revision = '2886fafea9d6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        op.f('ix_avatars_avatar_user_id'),
        'avatars', ['avatar_user_id'], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_avatars_avatar_user_id'), table_name='avatars')
    # ### end Alembic commands ###