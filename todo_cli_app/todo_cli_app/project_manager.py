from typing import List
from .models import Project

MAX_NUMBER_OF_PROJECTS = 5

class ProjectManager:
    def __init__(self):
        self.projects: List[Project] = []

    # (1)
    def add_project(self, name: str, description: str):
        if len(self.projects) >= MAX_NUMBER_OF_PROJECTS:
            print("❌ Error: Max number of projects reached.")
            return
        if any(p.name == name for p in self.projects):
            print("❌ Error: Project name already exists.")
            return
        if len(name) > 30:
            print("❌ Error: Project name too long.")
            return
        if len(description) > 150:
            print("❌ Error: Project description too long.")
            return

        project = Project(name, description)
        self.projects.append(project)
        print(f"✅ Project '{name}' added successfully!")

    # (2)
    def edit_project(self, old_name: str, new_name: str, new_desc: str):
        for p in self.projects:
            if p.name == old_name:
                if len(new_name) > 30:
                    print("❌ Error: Project name too long.")
                    return
                if len(new_desc) > 150:
                    print("❌ Error: Project description too long.")
                    return
                if any(pr.name == new_name for pr in self.projects if pr != p):
                    print("❌ Error: New name already exists.")
                    return
                p.name = new_name
                p.description = new_desc
                print(f"✅ Project '{old_name}' updated!")
                return
        print("❌ Error: Project not found.")

    # (3)
    def delete_project(self, name: str):
        for p in self.projects:
            if p.name == name:
                self.projects.remove(p)
                print(f"🗑️ Project '{name}' and all its tasks deleted!")
                return
        print("❌ Error: Project not found.")

    # (8)   
    def list_projects(self):
        if not self.projects:
            print("📭 No projects found.")
            return
        sorted_projects = sorted(self.projects, key=lambda p: p.created_at)
        for p in sorted_projects:
            print(f"📁 ID: {p.id} | {p.name} — {p.description} ({len(p.tasks)} tasks)")
