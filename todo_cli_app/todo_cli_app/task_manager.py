from datetime import datetime
from .models import Task, Project

MAX_NUMBER_OF_TASKS = 10

class TaskManager:
    def add_task(self, project: Project, title: str, description: str = "", status: str = "todo", deadline: str = None):
        if len(project.tasks) >= MAX_NUMBER_OF_TASKS:
            print("❌ Error: Max number of tasks reached.")
            return
        if len(title) > 30 or len(description) > 150:
            print("❌ Error: Text too long.")
            return
        if any(t.title == title for t in project.tasks):
            print("❌ Error: Task title already exists.")
            return
        if deadline:
            try:
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
                if deadline_date < datetime.now():
                    print("❌ Error: Deadline must be in the future.")
                    return
            except ValueError:
                print("❌ Error: Invalid date format (use YYYY-MM-DD).")
                return
        else:
            deadline_date = None

        task = Task(title, description, "todo", deadline_date)
        project.tasks.append(task)
        print(f"✅ Task '{title}' added to project '{project.name}'!")
