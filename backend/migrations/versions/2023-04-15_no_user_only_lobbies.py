"""no user, only lobbies

Revision ID: a19b28c7c902
Revises: cabb50b66b4c
Create Date: 2023-04-15 11:36:11.691843

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a19b28c7c902'
down_revision = 'cabb50b66b4c'
branch_labels = None
depends_on = None



def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('lobby_en_user_fkey', 'lobby_en', type_='foreignkey')
    op.drop_column('lobby_en', 'user')
    op.drop_constraint('lobby_ru_user_fkey', 'lobby_ru', type_='foreignkey')
    op.drop_column('lobby_ru', 'user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lobby_ru', sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('lobby_ru_user_fkey', 'lobby_ru', 'user', ['user'], ['username'])
    op.add_column('lobby_en', sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('lobby_en_user_fkey', 'lobby_en', 'user', ['user'], ['username'])
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=1024), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('username', name='user_username_key')
    )
    # ### end Alembic commands ###
