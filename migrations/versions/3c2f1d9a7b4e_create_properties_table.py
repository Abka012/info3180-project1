"""create properties table

Revision ID: 3c2f1d9a7b4e
Revises:
Create Date: 2026-03-23 10:55:00.000000
"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "3c2f1d9a7b4e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "properties",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("bedrooms", sa.Integer(), nullable=False),
        sa.Column("bathrooms", sa.Float(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("property_type", sa.String(length=20), nullable=False),
        sa.Column("location", sa.String(length=255), nullable=False),
        sa.Column("photo", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("properties")
