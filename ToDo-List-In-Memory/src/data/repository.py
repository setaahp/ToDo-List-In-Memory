from typing import List, Optional
from src.core.models import Project, Task
from datetime import datetime

MAX_NUMBER_OF_PROJECTS = 5
MAX_NUMBER_OF_TASKS = 10

class ProjectRepository:
    def __init__(self):
        self.projects: List[Project] = []

    # --- Project CRUD ---
    def add_project(self, project: Project) -> Project:
        if len(self.projects) >= MAX_NUMBER_OF_PROJECTS:
            raise ValueError("Max number of projects reached")
        if any(p.title == project.title for p in self.projects):
            raise ValueError("Project title exists")
        self.projects.append(project)
        return project

    def update_project(self, project_id: int, new_title: str, new_desc: Optional[str]) -> Project:
        project = self.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        project.title = new_title
        project.description = new_desc
        return project

    def delete_project(self, project_id: int) -> bool:
        project = self.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        self.projects.remove(project)
        return True

    def list_projects(self) -> List[Project]:
        return sorted(self.projects, key=lambda p: p.created_at)

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        return next((p for p in self.projects if p.id == project_id), None)

    # --- Task CRUD ---
    def add_task(self, project_id: int, task: Task) -> Task:
        project = self.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        if len(project.tasks) >= MAX_NUMBER_OF_TASKS:
            raise ValueError("Max tasks reached")
        task.project_id = project.id
        project.tasks.append(task)
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        for p in self.projects:
            for t in p.tasks:
                if t.id == task_id:
                    return t
        return None

    def update_task(self, task_id: int, title: str, description: Optional[str], deadline: Optional[datetime] = None) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        task.title = title
        task.description = description
        task.deadline = deadline
        return task

    def delete_task(self, task_id: int) -> bool:
        for p in self.projects:
            task = next((t for t in p.tasks if t.id == task_id), None)
            if task:
                p.tasks.remove(task)
                return True
        return False

    def change_task_status(self, task_id: int, new_status: str) -> Task:
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError("Task not found")
        task.change_status(new_status)
        return task

    def get_tasks_by_project(self, project_id: int) -> List[Task]:
        project = self.get_project_by_id(project_id)
        if not project:
            raise ValueError("Project not found")
        return sorted(project.tasks, key=lambda t: t.created_at)
