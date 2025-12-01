from datetime import datetime
from app.services.project_service import ProjectServiceDB
from app.services.task_service import TaskServiceDB

class CLIApp:
    def __init__(self, project_service: ProjectServiceDB, task_service: TaskServiceDB):
        self.project_service = project_service
        self.task_service = task_service

    def run(self):
        while True:
            print("\n--- TODO LIST ---")
            print("1. Add Project")
            print("2. Edit Project")
            print("3. Delete Project")
            print("4. Add Task")
            print("5. Change Task Status")
            print("6. Edit Task")
            print("7. Delete Task")
            print("8. List Projects")
            print("9. List Tasks of a Project")
            print("10. Show Overdue Tasks")
            print("11. Close Overdue Tasks Now")
            print("0. Exit")

            choice = input("> ")

            if choice == "1":
                name = input("Project name: ")
                desc = input("Description: ")
                try:
                    project = self.project_service.create_project(name, desc)
                    print(f"✅ Project '{project.title}' created with ID {project.id}!")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "2":
                pid_input = input("Project ID: ")
                try:
                    pid = int(pid_input)
                except ValueError:
                    print("❌ Invalid project ID")
                    continue
                new_name = input("New project name: ")
                new_desc = input("New description: ")
                try:
                    self.project_service.update_project(pid, new_name, new_desc)
                    print("✅ Project updated!")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "3":
                pid_input = input("Project ID to delete: ")
                try:
                    pid = int(pid_input)
                except ValueError:
                    print("❌ Invalid project ID")
                    continue
                try:
                    self.project_service.delete_project(pid)
                    print("🗑️ Project deleted!")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "4":
                pid_input = input("Project ID: ")
                try:
                    pid = int(pid_input)
                except ValueError:
                    print("❌ Invalid project ID")
                    continue
                title = input("Task title: ")
                desc = input("Task description: ")
                deadline_input = input("Deadline (YYYY-MM-DD or empty): ")
                if deadline_input:
                    try:
                        deadline = datetime.strptime(deadline_input, "%Y-%m-%d")
                    except ValueError:
                        print("❌ Invalid date format! Use YYYY-MM-DD.")
                        continue
                else:
                    deadline = None
                try:
                    task = self.task_service.add_task_to_project(pid, title, desc, deadline)
                    print(f"✅ Task '{task.title}' added with ID {task.id}!")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "5":
                tid_input = input("Task ID: ")
                try:
                    tid = int(tid_input)
                except ValueError:
                    print("❌ Invalid task ID")
                    continue
                new_status = input("New status (todo/doing/done): ")
                try:
                    self.task_service.change_task_status(tid, new_status)
                    print("🔄 Task status updated!")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "6":
                tid_input = input("Task ID: ")
                try:
                    tid = int(tid_input)
                except ValueError:
                    print("❌ Invalid task ID")
                    continue
                new_desc = input("New description (or empty): ") or None
                new_deadline_input = input("New deadline (YYYY-MM-DD or empty): ")
                if new_deadline_input:
                    try:
                        new_deadline = datetime.strptime(new_deadline_input, "%Y-%m-%d")
                    except ValueError:
                        print("❌ Invalid date format! Use YYYY-MM-DD.")
                        continue
                else:
                    new_deadline = None
                try:
                    task = self.task_service.get_task(tid)
                    if not task:
                        print("❌ Task not found.")
                        continue
                    self.task_service.update_task(tid, task.title, new_desc, new_deadline)
                    print("✏️ Task updated successfully!")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "7":
                tid_input = input("Task ID to delete: ")
                try:
                    tid = int(tid_input)
                except ValueError:
                    print("❌ Invalid task ID")
                    continue
                try:
                    self.task_service.delete_task(tid)
                    print("🗑️ Task deleted!")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "8":
                projects = self.project_service.list_projects()
                if not projects:
                    print("📭 No projects found.")
                for p in projects:
                    print(f"📁 ID: {p.id} | {p.title} — {p.description} ({len(p.tasks)} tasks)")

            elif choice == "9":
                pid_input = input("Project ID: ")
                try:
                    pid = int(pid_input)
                except ValueError:
                    print("❌ Invalid project ID")
                    continue
                try:
                    tasks = self.task_service.list_tasks_by_project(pid)
                    if not tasks:
                        print("📭 No tasks for this project.")
                    for t in tasks:
                        deadline_str = t.deadline.strftime("%Y-%m-%d") if t.deadline else "—"
                        print(f"  ID: {t.id} | {t.title} [{t.status}] | Deadline: {deadline_str}")
                except ValueError as e:
                    print(f"❌ {e}")
            elif choice == "10":  # How overdue tasks
                try:
                    overdue_tasks = self.task_service.get_overdue_tasks()
                    if not overdue_tasks:
                        print("📭 No overdue tasks.")
                    for t in overdue_tasks:
                        deadline_str = t.deadline.strftime("%Y-%m-%d") if t.deadline else "—"
                        print(f"  ID: {t.id} | {t.title} [{t.status}] | Deadline: {deadline_str}")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "11":  # Close overdue tasks now
                try:
                    success, message = self.task_service.close_overdue_tasks()
                    print(f"✅ {message}")
                except ValueError as e:
                    print(f"❌ {e}")
            elif choice == "10":  # How overdue tasks
                try:
                    overdue_tasks = self.task_service.get_overdue_tasks()
                    if not overdue_tasks:
                        print("📭 No overdue tasks.")
                    for t in overdue_tasks:
                        deadline_str = t.deadline.strftime("%Y-%m-%d") if t.deadline else "—"
                        print(f"  ID: {t.id} | {t.title} [{t.status}] | Deadline: {deadline_str}")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "11":  # Close overdue tasks now
                try:
                    success, message = self.task_service.close_overdue_tasks()
                    print(f"✅ {message}")
                except ValueError as e:
                    print(f"❌ {e}")

            elif choice == "0":
                break

            else:
                print("❌ Invalid option.")
