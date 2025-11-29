from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    tasks = relationship("Task", back_populates="project", cascade="all, delete")
