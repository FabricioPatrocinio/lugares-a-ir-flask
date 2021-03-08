"""empty message

Revision ID: e4296d16bb9f
Revises: 
Create Date: 2021-03-08 09:38:20.894077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4296d16bb9f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('senha', sa.String(length=255), nullable=False),
    sa.Column('img_perfil', sa.String(length=255), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('publicacao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('regiao', sa.String(length=100), nullable=False),
    sa.Column('nome_local', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.String(length=2000), nullable=True),
    sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('imagens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('publicacao_id', sa.Integer(), nullable=True),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.ForeignKeyConstraint(['publicacao_id'], ['publicacao.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('imagens')
    op.drop_table('publicacao')
    op.drop_table('user')
    # ### end Alembic commands ###
