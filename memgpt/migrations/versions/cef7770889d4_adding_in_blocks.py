"""adding in blocks

Revision ID: cef7770889d4
Revises: bc9a9070791e
Create Date: 2024-08-12 18:10:29.885208

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from memgpt.orm.block import BlockValue

# revision identifiers, used by Alembic.
revision: str = 'cef7770889d4'
down_revision: Union[str, None] = 'bc9a9070791e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table('tools_presets')
    op.drop_table('sources_presets')
    op.drop_table('preset')
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('block',
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('label', sa.String(), nullable=False),
    sa.Column('is_template', sa.Boolean(), nullable=False),
    sa.Column('value', BlockValue(astext_type=sa.Text()), nullable=True),
    sa.Column('limit', sa.Integer(), nullable=False),
    sa.Column('metadata_', sa.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('_organization_id', sa.UUID(), nullable=True),
    sa.Column('_id', sa.UUID(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.Column('_created_by_id', sa.UUID(), nullable=True),
    sa.Column('_last_updated_by_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['_organization_id'], ['organization._id'], ),
    sa.PrimaryKeyConstraint('label', '_id')
    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sources_presets',
    sa.Column('_preset_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('_source_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['_preset_id'], ['preset._id'], name='sources_presets__preset_id_fkey'),
    sa.ForeignKeyConstraint(['_source_id'], ['source._id'], name='sources_presets__source_id_fkey'),
    sa.PrimaryKeyConstraint('_preset_id', '_source_id', name='sources_presets_pkey')
    )
    op.create_table('preset',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('human_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('persona_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('functions_schema', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False),
    sa.Column('_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('deleted', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('is_deleted', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.Column('_created_by_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('_last_updated_by_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('_organization_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('system_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('_human_memory_template_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('_persona_memory_template_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('_system_memory_template_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['_human_memory_template_id'], ['memory_template._id'], name='preset__human_memory_template_id_fkey'),
    sa.ForeignKeyConstraint(['_organization_id'], ['organization._id'], name='preset__organization_id_fkey'),
    sa.ForeignKeyConstraint(['_persona_memory_template_id'], ['memory_template._id'], name='preset__persona_memory_template_id_fkey'),
    sa.ForeignKeyConstraint(['_system_memory_template_id'], ['memory_template._id'], name='preset__system_memory_template_id_fkey'),
    sa.PrimaryKeyConstraint('_id', name='preset_pkey'),
    sa.UniqueConstraint('_organization_id', 'name', name='unique_name_organization'),
    postgresql_ignore_search_path=False
    )
    op.create_table('tools_presets',
    sa.Column('_preset_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('_tool_id', sa.UUID(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['_preset_id'], ['preset._id'], name='tools_presets__preset_id_fkey'),
    sa.ForeignKeyConstraint(['_tool_id'], ['tool._id'], name='tools_presets__tool_id_fkey'),
    sa.PrimaryKeyConstraint('_preset_id', '_tool_id', name='tools_presets_pkey')
    )
    op.drop_table('block')
    # ### end Alembic commands ###
