from .project_manager import ProjectManager
from .task_manager import TaskManager

def main():
    pm = ProjectManager()
    tm = TaskManager()

    while True:
        print("\n--- TODO CLI ---")
        print("1. Add Project")
        print("2. Edit Project")
        print("3. Delete Project")
        print("4. Add Task")
        print("5. Show Projects")
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
            for p in pm.projects:
                print(f"\n📁 {p.name} — {len(p.tasks)} tasks")
                for t in p.tasks:
                    print(f"  - {t.title} [{t.status}]")
        elif choice == "0":
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
