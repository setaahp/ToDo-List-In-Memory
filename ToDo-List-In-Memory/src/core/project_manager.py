from src.core.models import Project

class ProjectManager:
    def __init__(self):
        self.projects = []

    def create_project(self, name: str):
        project = Project(name)
        self.projects.append(project)
        return project

    def list_projects(self):
        return self.projects

    def get_project(self, pid: int):
        for p in self.projects:
            if p.id == pid:
                return p
        return None
