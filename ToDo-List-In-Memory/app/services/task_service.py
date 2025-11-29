# task_service.py
from typing import List, Optional
from datetime import datetime
from app.models.task import Task
from app.repositories.task_repository import TaskRepositoryDB
from app.repositories.project_repository import ProjectRepositoryDB
from sqlalchemy.orm import Session

MAX_NUMBER_OF_TASKS = 10

class TaskServiceDB:
    def __init__(self, db_session: Session):
        self.project_repo = ProjectRepositoryDB(db_session)
        self.repo = TaskRepositoryDB(db_session)

    # --- Task CRUD ---
    def add_task_to_project(self, project_id: int, title: str, description: Optional[str] = None,
                            deadline: Optional[datetime] = None) -> Task:
        project = self.project_repo.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        task_count = len(self.repo.get_tasks_by_project(project_id))
        if task_count >= MAX_NUMBER_OF_TASKS:
            raise ValueError("Max number of tasks reached")
        task = Task(title=title, description=description, deadline=deadline, project_id=project_id)
        return self.repo.add_task(project_id, task)

    def update_task(self, task_id: int, title: str, description: Optional[str] = None,
                    deadline: Optional[datetime] = None) -> Task:
        return self.repo.update_task(task_id, title, description, deadline)

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.repo.get_task_by_id(task_id)

    def delete_task(self, task_id: int) -> bool:
        return self.repo.delete_task(task_id)

    def change_task_status(self, task_id: int, new_status: str) -> Task:
        return self.repo.change_task_status(task_id, new_status)

    def list_tasks_by_project(self, project_id: int) -> List[Task]:
        return self.repo.get_tasks_by_project(project_id)
