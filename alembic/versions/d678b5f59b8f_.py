"""empty message

Revision ID: d678b5f59b8f
Revises: a3cf7cb93427
Create Date: 2025-06-19 12:08:25.055869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'd678b5f59b8f'
down_revision: Union[str, Sequence[str], None] = 'a3cf7cb93427'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('podcastepisode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('track_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('episode_url', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.Column('collection_name', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('collection_id', sa.Integer(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('artwork_url_600', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('user_interactions', sa.Integer(), nullable=False),
    sa.Column('last_user_interaction', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('podcastepisode', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_podcastepisode_collection_id'), ['collection_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_podcastepisode_track_id'), ['track_id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('podcastepisode', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_podcastepisode_track_id'))
        batch_op.drop_index(batch_op.f('ix_podcastepisode_collection_id'))

    op.drop_table('podcastepisode')
    # ### end Alembic commands ###
