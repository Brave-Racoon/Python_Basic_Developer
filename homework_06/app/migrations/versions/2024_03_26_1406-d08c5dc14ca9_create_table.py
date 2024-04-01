"""create table

Revision ID: d08c5dc14ca9
Revises: 
Create Date: 2024-03-26 14:06:28.363370

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d08c5dc14ca9"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "products",
        sa.Column("title", sa.String(length=64), nullable=False),
        sa.Column(
            "description", sa.String(length=255), nullable=False
        ),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("discountPercentage", sa.Float(), nullable=False),
        sa.Column("rating", sa.Float(), nullable=False),
        sa.Column("stock", sa.Integer(), nullable=False),
        sa.Column("brand", sa.String(length=255), nullable=False),
        sa.Column(
            "id", sa.Integer(), autoincrement=True, nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("products")
    # ### end Alembic commands ###
