# app/api/schemas.py
from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime

# -------------------
# Project Schemas
# -------------------

class ProjectBase(BaseModel):
    title: str = Field(..., example="My Project")
    description: Optional[str] = Field(None, example="Project description")

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class ProjectOut(ProjectBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# -------------------
# Task Schemas
# -------------------

class TaskBase(BaseModel):
    title: str = Field(..., example="My Task")
    description: Optional[str] = None
    status: Optional[str] = Field("todo", example="todo")  # "todo", "doing", "done"
    deadline: Optional[datetime] = None
    project_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    deadline: Optional[datetime] = None
    project_id: Optional[int] = None

class TaskOut(TaskBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
