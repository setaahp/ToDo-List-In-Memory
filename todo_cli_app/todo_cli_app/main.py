from .project_manager import ProjectManager
from .task_manager import TaskManager

def main():
    pm = ProjectManager()
    tm = TaskManager()

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
        print("0. Exit")
        choice = input("> ")

        if choice == "1":
            name = input("Project name: ")
            desc = input("Description: ")
            pm.add_project(name, desc)

        elif choice == "2":
            old = input("Old name: ")
            new = input("New name: ")
            desc = input("New description: ")
            pm.edit_project(old, new, desc)

        elif choice == "3":
            name = input("Project name to delete: ")
            pm.delete_project(name)

        elif choice == "4":
            pname = input("Project name: ")
            project = next((p for p in pm.projects if p.name == pname), None)
            if not project:
                print("❌ Project not found.")
                continue
            title = input("Task title: ")
            desc = input("Task description: ")
            deadline = input("Deadline (YYYY-MM-DD or empty): ")
            tm.add_task(project, title, desc, deadline=deadline or None)

        elif choice == "5":
            pname = input("Project name: ")
            project = next((p for p in pm.projects if p.name == pname), None)
            if not project:
                print("❌ Project not found.")
                continue
            tid = int(input("Task ID: "))
            new_status = input("New status (todo/doing/done): ")
            tm.change_status(project, tid, new_status)

        elif choice == "6":
            pname = input("Project name: ")
            project = next((p for p in pm.projects if p.name == pname), None)
            if not project:
                print("❌ Project not found.")
                continue
            tid = int(input("Task ID: "))
            desc = input("New description (or empty): ")
            deadline = input("New deadline (YYYY-MM-DD or empty): ")
            status = input("New status (todo/doing/done or empty): ")
            tm.edit_task(project, tid, desc or None, deadline or None, status or None)

        elif choice == "7":
            pname = input("Project name: ")
            project = next((p for p in pm.projects if p.name == pname), None)
            if not project:
                print("❌ Project not found.")
                continue
            tid = int(input("Task ID to delete: "))
            tm.delete_task(project, tid)

        elif choice == "8":
            pm.list_projects()

        elif choice == "9":
            pname = input("Project name: ")
            project = next((p for p in pm.projects if p.name == pname), None)
            if not project:
                print("❌ Project not found.")
                continue
            tm.list_tasks(project)

        elif choice == "0":
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
