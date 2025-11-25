from src.core.models import Task

class TaskManager:
    def create_task(self, project, title: str, description=""):
        task = Task(title, description)
        project.tasks.append(task)
        return task

    def list_tasks(self, project):
        return project.tasks
