# project_repository.py
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.project import Project

MAX_NUMBER_OF_PROJECTS = 5

class ProjectRepositoryDB:
    def __init__(self, db_session: Session):
        self.db = db_session

    # --- Project CRUD ---
    def add_project(self, project: Project) -> Project:
        total_projects = self.db.query(Project).count()
        if total_projects >= MAX_NUMBER_OF_PROJECTS:
            raise ValueError("Max number of projects reached")
        if self.db.query(Project).filter_by(title=project.title).first():
            raise ValueError("Project title exists")
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def update_project(self, project_id: int, updates: dict) -> Project:
        project = self.db.query(Project).filter_by(id=project_id).first()
        if not project:
            return None
        for key, value in updates.items():
            setattr(project, key, value)

        self.db.commit()
        self.db.refresh(project)
        return project


    def delete_project(self, project_id: int) -> bool:
        project = self.db.query(Project).filter_by(id=project_id).first()
        if not project:
            raise ValueError("Project not found")
        self.db.delete(project)
        self.db.commit()
        return True

    def list_projects(self) -> List[Project]:
        return self.db.query(Project).order_by(Project.created_at).all()

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        return self.db.query(Project).filter_by(id=project_id).first()
