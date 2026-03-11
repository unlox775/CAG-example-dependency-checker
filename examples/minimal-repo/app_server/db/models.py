"""SQLAlchemy models."""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from db.connection import Base


class ExportRecord(Base):
    __tablename__ = "export_records"

    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String(255), nullable=False)
    row_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
