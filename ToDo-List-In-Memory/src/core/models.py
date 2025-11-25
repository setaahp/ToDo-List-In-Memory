from datetime import datetime
from typing import Optional, List

# --- Project Model ---
class Project:
    next_id = 1

    def __init__(self, title: str, description: Optional[str] = None):
        self.id = Project.next_id
        Project.next_id += 1

        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.tasks: List["Task"] = []

# --- Task Model ---
class Task:
    next_id = 1

    def __init__(self, title: str, description: Optional[str] = None, deadline: Optional[datetime] = None):
        self.id = Task.next_id
        Task.next_id += 1

        self.title = title
        self.description = description
        self.status = "todo"
        self.deadline = deadline
        self.created_at = datetime.now()
        self.project_id: int

    def change_status(self, new_status: str):
        if new_status not in ["todo", "doing", "done"]:
            raise ValueError(f"Invalid status: {new_status}")
        self.status = new_status
