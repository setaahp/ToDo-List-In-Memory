# project_service.py
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.project import Project
from app.repositories.project_repository import ProjectRepositoryDB

class ProjectServiceDB:
    def __init__(self, db_session: Session):
        self.db = db_session
        self.repo = ProjectRepositoryDB(db_session)

    # --- Project CRUD ---
    def create_project(self, title: str, description: Optional[str] = None) -> Project:
        project = Project(title=title, description=description)
        return self.repo.add_project(project)

    def update_project(self, project_id: int, updates: dict) -> Project:
        return self.repo.update_project(project_id, updates)

    def delete_project(self, project_id: int) -> bool:
        return self.repo.delete_project(project_id)

    def list_projects(self) -> List[Project]:
        return self.repo.list_projects()

    def get_project(self, project_id: int) -> Optional[Project]:
        return self.repo.get_project_by_id(project_id)
