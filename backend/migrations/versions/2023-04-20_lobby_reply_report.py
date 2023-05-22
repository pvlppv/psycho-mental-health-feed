"""lobby, reply, report

Revision ID: 65d3d54a9e59
Revises: a19b28c7c902
Create Date: 2023-04-20 20:46:26.505342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65d3d54a9e59'
down_revision = 'a19b28c7c902'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('lobby',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lobby_name', sa.String(), nullable=True),
    sa.Column('message_text', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['lobby_name'], ['lobby.name'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_message_lobby_name'), 'message', ['lobby_name'], unique=False)
    op.create_table('reply',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=True),
    sa.Column('reply_text', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reply_message_id'), 'reply', ['message_id'], unique=False)
    op.create_table('report',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message_id', sa.Integer(), nullable=True),
    sa.Column('report_text', sa.String(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['message.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_report_message_id'), 'report', ['message_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_report_message_id'), table_name='report')
    op.drop_table('report')
    op.drop_index(op.f('ix_reply_message_id'), table_name='reply')
    op.drop_table('reply')
    op.drop_index(op.f('ix_message_lobby_name'), table_name='message')
    op.drop_table('message')
    op.drop_table('lobby')
    # ### end Alembic commands ###
