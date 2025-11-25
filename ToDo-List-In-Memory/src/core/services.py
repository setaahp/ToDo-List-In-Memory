from datetime import datetime
from typing import Optional, List
from src.core.models import Project, Task
from src.data.repository import ProjectRepository

MAX_NUMBER_OF_TASKS = 10

class ToDoService:
    def __init__(self, repository: ProjectRepository):
        self._repo = repository

    # --- Project CRUD ---
    def create_project(self, title: str, description: Optional[str] = None) -> Project:
        project = Project(title=title, description=description)
        return self._repo.add_project(project)

    def update_project(self, project_id: int, new_title: str, new_desc: Optional[str]) -> Project:
        return self._repo.update_project(project_id, new_title, new_desc)

    def delete_project(self, project_id: int) -> bool:
        return self._repo.delete_project(project_id)

    def list_projects(self) -> List[Project]:
        return self._repo.list_projects()

    # --- Task CRUD ---
    def add_task_to_project(self, project_id: int, title: str, description: Optional[str] = None,
                    deadline: Optional[datetime] = None) -> Task:
        project = self._repo.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        if len(project.tasks) >= MAX_NUMBER_OF_TASKS:
            raise ValueError("Max number of tasks reached")
        task = Task(title, description, deadline)
        return self._repo.add_task(project_id, task)

    def update_task(self, task_id: int, title: str, description: Optional[str] = None,
                    deadline: Optional[datetime] = None) -> Task:
        return self._repo.update_task(task_id, title, description, deadline)
    
    def get_task(self, task_id: int) -> Optional[Task]:
        return self._repo.get_task_by_id(task_id)
    
    def delete_task(self, task_id: int) -> bool:
        return self._repo.delete_task(task_id)

    def change_task_status(self, task_id: int, new_status: str) -> Task:
        return self._repo.change_task_status(task_id, new_status)

    def list_tasks_by_project(self, project_id: int) -> List[Task]:
        return self._repo.get_tasks_by_project(project_id)
