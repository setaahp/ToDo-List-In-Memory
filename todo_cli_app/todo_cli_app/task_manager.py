from datetime import datetime
from .models import Task, Project

MAX_NUMBER_OF_TASKS = 10
VALID_STATUSES = ["todo", "doing", "done"]

class TaskManager:
    # (4)
    def add_task( self, project: Project, title: str, description: str = "", status: str = "todo", deadline: str | None = None):
        if len(project.tasks) >= MAX_NUMBER_OF_TASKS:
            print("❌ Error: Max number of tasks reached.")
            return
        if len(title) > 30:
            print("❌ Error: Task name too long.")
            return
        if len(description) > 150:
            print("❌ Error: Task description too long.")
        if any(t.title == title for t in project.tasks):
            print("❌ Error: Task title already exists.")
            return
        if deadline:
            try:
                deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
                if deadline_date < datetime.now():
                    print("❌ Error: Deadline must be in the future!")
                    return
            except ValueError:
                print("❌ Error: Invalid date format (use YYYY-MM-DD).")
                return
        else:
            deadline_date = None

        task = Task(title, description, "todo", deadline_date)
        project.tasks.append(task)
        print(f"✅ Task '{title}' added to project '{project.name}'!")

    # (5)  
    def change_status(self, project: Project, task_id: int, new_status: str):
        task = next((t for t in project.tasks if t.id == task_id), None)
        if not task:
            print("❌ Task not found.")
            return
        if new_status not in VALID_STATUSES:
            print("❌ Invalid status. Choose from: todo, doing, done")
            return
        #  todo → doing → done 
        order = {"todo": 0, "doing": 1, "done": 2}
        if order[new_status] < order[task.status]:
            print("❌ Invalid status transition (cannot go backwards).")
            return

        task.status = new_status
        print(f"🔄 Task '{task.title}' status changed to '{new_status}'.")

    # (6) 
    def edit_task(self, project: Project, task_id: int, new_desc: str | None = None, new_deadline: str | None = None, new_status: str | None = None):
        task = next((t for t in project.tasks if t.id == task_id), None)
        if not task:
            print("❌ Task not found.")
            return

        if new_desc and len(new_desc) > 150:
            print("❌ Error: Description too long.")
            return

        if new_status:
            if new_status not in VALID_STATUSES:
                print("❌ Invalid status.")
                return
            order = {"todo": 0, "doing": 1, "done": 2}
            if order[new_status] < order[task.status]:
                print("❌ Invalid status transition.")
                return
            task.status = new_status

        if new_deadline:
            try:
                deadline_date = datetime.strptime(new_deadline, "%Y-%m-%d")
                if deadline_date < datetime.now():
                    print("❌ Deadline must be in the future.")
                    return
                task.deadline = deadline_date
            except ValueError:
                print("❌ Invalid date format.")
                return

        if new_desc:
            task.description = new_desc

        print(f"✏️ Task '{task.title}' updated successfully!")

    # (7) 
    def delete_task(self, project: Project, task_id: int):
        for t in project.tasks:
            if t.id == task_id:
                project.tasks.remove(t)
                print(f"🗑️ Task '{t.title}' deleted from project '{project.name}'.")
                return
        print("❌ Task not found.")

    # (9)  
    def list_tasks(self, project: Project):
        if not project.tasks:
            print("📭 No tasks found for this project.")
            return
        sorted_tasks = sorted(project.tasks, key=lambda t: t.created_at)
        print(f"\n📋 Tasks for project '{project.name}':")
        for t in sorted_tasks:
            deadline_str = t.deadline.strftime("%Y-%m-%d") if t.deadline else "—"
            print(f"  ID: {t.id} | {t.title} [{t.status}] | Deadline: {deadline_str}")
