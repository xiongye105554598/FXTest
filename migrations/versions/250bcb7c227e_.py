"""empty message

Revision ID: 250bcb7c227e
Revises: 
Create Date: 2017-11-20 15:34:05.509465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '250bcb7c227e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('makeuser', sa.Integer(), nullable=True),
    sa.Column('taskname', sa.String(length=52), nullable=True),
    sa.Column('taskdesc', sa.String(length=252), nullable=True),
    sa.Column('taskstart', sa.String(length=252), nullable=True),
    sa.Column('taskmakedate', sa.DateTime(), nullable=True),
    sa.Column('taskrepor_to', sa.String(length=252), nullable=True),
    sa.Column('taskrepor_cao', sa.String(length=252), nullable=True),
    sa.Column('task_make_email', sa.String(length=252), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('yunxing_status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['makeuser'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registrations',
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('interfacetests_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['interfacetests_id'], ['interfacetests.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], )
    )
    op.create_foreign_key(None, 'tstresults', 'projects', ['projects_id'], ['id'])
    op.create_foreign_key(None, 'users', 'roles', ['role_id'], ['id'])
    op.create_foreign_key(None, 'users', 'works', ['work_id'], ['id'])
    op.drop_column('users', 'level')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('level', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'tstresults', type_='foreignkey')
    op.drop_table('registrations')
    op.drop_table('tasks')
    # ### end Alembic commands ###