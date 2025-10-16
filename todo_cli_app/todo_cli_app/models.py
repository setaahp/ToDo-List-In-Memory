from datetime import datetime
from typing import List, Optional

class Task:
    def __init__(self, title: str, description: str = "", status: str = "todo", deadline: Optional[datetime] = None):
        self.title = title
        self.description = description
        self.status = status
        self.deadline = deadline

class Project:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.tasks: List[Task] = []
