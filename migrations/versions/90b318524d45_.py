"""empty message

Revision ID: 90b318524d45
Revises: 
Create Date: 2023-05-15 20:38:09.265790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90b318524d45'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('userID'),
    sa.UniqueConstraint('email')
    )
    op.create_table('conversations',
    sa.Column('conversationID', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('conv_json', sa.Text(), nullable=True),
    sa.Column('userID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['userID'], ['user.userID'], ),
    sa.PrimaryKeyConstraint('conversationID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('conversations')
    op.drop_table('user')
    # ### end Alembic commands ###