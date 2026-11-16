"""Create items table"""
from alembic import op
import sqlalchemy as sa
revision = "0001"
down_revision = None
branch_labels = None
depends_on = None
def upgrade():
    op.create_table("items", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("name", sa.String(150), nullable=False), sa.Column("description", sa.String(500), nullable=False, server_default=""))
def downgrade():
    op.drop_table("items")
