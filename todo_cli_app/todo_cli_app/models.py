from datetime import datetime
from typing import List, Optional

class Task:
    next_id = 1

    def __init__(self, title: str, description: str = "", status: str = "todo", deadline: Optional[datetime] = None):
        self.id = Task.next_id
        Task.next_id += 1

        self.title = title
        self.description = description
        self.status = status
        self.deadline = deadline
        self.created_at = datetime.now()

class Project:
    next_id = 1

    def __init__(self, name: str, description: str = ""):
        self.id = Project.next_id
        Project.next_id += 1

        self.name = name
        self.description = description
        self.tasks: List[Task] = []
        self.created_at = datetime.now()
