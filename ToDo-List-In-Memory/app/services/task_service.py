# task_service.py

from typing import List, Optional
from datetime import datetime
from app.models.task import Task
from app.repositories.task_repository import TaskRepositoryDB
from app.repositories.project_repository import ProjectRepositoryDB
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

MAX_NUMBER_OF_TASKS = 10
VALID_STATUSES = {"todo", "doing", "done"}

class TaskServiceDB:
    def __init__(self, db_session: Session):
        self.db = db_session
        self.project_repo = ProjectRepositoryDB(db_session)
        self.repo = TaskRepositoryDB(db_session)

    # Create task in a project
    def add_task_to_project(self, project_id: int, data: dict) -> Task:
        project = self.project_repo.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")

        task_count = len(self.repo.get_tasks_by_project(project_id))
        if task_count >= MAX_NUMBER_OF_TASKS:
            raise ValueError("Max number of tasks reached")

        task = Task(
            title=data.get("title"),
            description=data.get("description"),
            deadline=data.get("deadline"),
            project_id=project_id
    )

        return self.repo.add_task(project_id, task)

    # Update task
    def update_task(self, task_id: int, updates: dict) -> Task:
        task = self.repo.get_task_by_id(task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

    # 1) STATUS VALIDATION
        if "status" in updates:
            new_status = updates["status"]

        if new_status not in VALID_STATUSES:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid status '{new_status}'. Allowed: {VALID_STATUSES}"
            )

        old_status = task.status

        if old_status == "done":
            raise HTTPException(
                status_code=400,
                detail="Completed tasks cannot be modified"
            )

        if old_status == "doing" and new_status == "todo":
            raise HTTPException(
                status_code=400,
                detail="A task in 'doing' cannot be moved back to 'todo'"
            )

    # 2) DEADLINE VALIDATION
        if "deadline" in updates:
            if updates["deadline"] < datetime.now():
                raise HTTPException(
                status_code=400,
                detail="Deadline cannot be in the past"
            )

    # 3) APPLY UPDATE
        updated_task = self.repo.update_task(task_id, updates)
        return updated_task

    # Get task
    def get_task(self, task_id: int) -> Optional[Task]:
        return self.repo.get_task_by_id(task_id)

    # Delete task
    def delete_task(self, task_id: int) -> bool:
        return self.repo.delete_task(task_id)

    # Change task status
    def change_task_status(self, task_id: int, new_status: str) -> Task:
        return self.repo.change_task_status(task_id, new_status)

    # List tasks for project
    def list_tasks_by_project(self, project_id: int) -> List[Task]:
        return self.repo.get_tasks_by_project(project_id)

    def get_overdue_tasks(self):
        now = datetime.now()
        return self.db.query(Task).filter(Task.deadline < now, Task.status != "done").all()
    
    def close_overdue_tasks(self) -> tuple[bool, str]:
        """Set status='done' and closed_at=now for all overdue tasks"""
        overdue_tasks = self.get_overdue_tasks()
        if not overdue_tasks:
            return False, "No overdue tasks to close."
        for task in overdue_tasks:
            task.status = "done"
            task.closed_at = datetime.now()
            self.repo.update_task(task.id, task.title, task.description, task.deadline)
        return True, f"{len(overdue_tasks)} overdue tasks closed."

