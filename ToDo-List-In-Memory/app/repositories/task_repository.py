# task_repository.py
from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.project import Project

MAX_NUMBER_OF_TASKS = 10

class TaskRepositoryDB:
    def __init__(self, db_session: Session):
        self.db = db_session

    def add_task(self, project_id: int, task: Task) -> Task:
        project = self.db.query(Project).filter_by(id=project_id).first()
        if not project:
            return None

        task_count = self.db.query(Task).filter_by(project_id=project_id).count()
        if task_count >= MAX_NUMBER_OF_TASKS:
            return None

        task.project_id = project.id
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task


    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        return self.db.query(Task).filter_by(id=task_id).first()

    def update_task(self, task_id: int, updates: dict) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            return None

        for key, value in updates.items():
            setattr(task, key, value)

        self.db.commit()
        self.db.refresh(task)
        return task


    def delete_task(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        self.db.delete(task)
        self.db.commit()
        return True

    def change_task_status(self, task_id: int, new_status: str) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        task.change_status(new_status)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_tasks_by_project(self, project_id: int) -> List[Task]:
        project = self.db.query(Project).filter_by(id=project_id).first()
        if not project:
            raise ValueError("Project not found")
        return self.db.query(Task).filter_by(project_id=project_id).order_by(Task.created_at).all()

    def get_tasks_by_filter(self, filter_func):
        """Return all tasks matching a filter function"""
        tasks = self.db.query(Task).all()
        return [t for t in tasks if filter_func(t)]

    def save(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

