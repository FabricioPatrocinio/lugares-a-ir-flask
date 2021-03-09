"""empty message

Revision ID: 17303fbe3cc3
Revises: e4296d16bb9f
Create Date: 2021-03-09 14:29:00.414379

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '17303fbe3cc3'
down_revision = 'e4296d16bb9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('fk_Cidade_estado', table_name='cidades')
    op.create_foreign_key(None, 'cidades', 'estados', ['id_estado'], ['id'])
    op.add_column('publicacao', sa.Column('Cidades', sa.Integer(), nullable=True))
    op.alter_column('publicacao', 'nome_local',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.create_foreign_key(None, 'publicacao', 'cidades', ['Cidades'], ['id'])
    op.drop_column('publicacao', 'regiao')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('publicacao', sa.Column('regiao', mysql.VARCHAR(length=100), nullable=False))
    op.drop_constraint(None, 'publicacao', type_='foreignkey')
    op.alter_column('publicacao', 'nome_local',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.drop_column('publicacao', 'Cidades')
    op.drop_constraint(None, 'cidades', type_='foreignkey')
    op.create_index('fk_Cidade_estado', 'cidades', ['id_estado'], unique=False)
    # ### end Alembic commands ###