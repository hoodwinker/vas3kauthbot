"""Add RequestText

Revision ID: 79092a5bfdc6
Revises: c155354c1ae6
Create Date: 2024-05-13 13:11:41.605697

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '79092a5bfdc6'
down_revision = 'c155354c1ae6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request_texts',
                    sa.Column('chat_id', sa.BigInteger(), nullable=False),
                    sa.Column('text', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('chat_id')
                    )
    op.add_column('chats', sa.Column('follow_up_requests',
                                     sa.Boolean(), default=False, nullable=True))

    op.alter_column('chats', 'show_intro',
                    existing_type=sa.BOOLEAN(),
                    nullable=False)
    op.alter_column('chats', 'only_active',
                    existing_type=sa.BOOLEAN(),
                    nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('chats', 'only_active',
                    existing_type=sa.BOOLEAN(),
                    nullable=True)
    op.alter_column('chats', 'show_intro',
                    existing_type=sa.BOOLEAN(),
                    nullable=True)
    op.drop_column('chats', 'follow_up_requests')
    op.drop_table('request_texts')
    # ### end Alembic commands ###
