from typing import List
from .models import Project

MAX_NUMBER_OF_PROJECTS = 5

class ProjectManager:
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, name: str, description: str):
        if len(self.projects) >= MAX_NUMBER_OF_PROJECTS:
            print("❌ Error: Max number of projects reached.")
            return
        if any(p.name == name for p in self.projects):
            print("❌ Error: Project name already exists.")
            return
        if len(name) > 30 or len(description) > 150:
            print("❌ Error: Project name/description too long.")
            return

        project = Project(name, description)
        self.projects.append(project)
        print(f"✅ Project '{name}' added successfully!")

    def edit_project(self, old_name: str, new_name: str, new_desc: str):
        for p in self.projects:
            if p.name == old_name:
                if len(new_name) > 30 or len(new_desc) > 150:
                    print("❌ Error: Text too long.")
                    return
                if any(pr.name == new_name for pr in self.projects if pr != p):
                    print("❌ Error: New name already exists.")
                    return
                p.name = new_name
                p.description = new_desc
                print(f"✅ Project '{old_name}' updated!")
                return
        print("❌ Error: Project not found.")

    def delete_project(self, name: str):
        for p in self.projects:
            if p.name == name:
                self.projects.remove(p)
                print(f"🗑️ Project '{name}' and all its tasks deleted!")
                return
        print("❌ Error: Project not found.")
