from src.data.repository import ProjectRepository
from src.core.services import ToDoService
from src.cli.cli_app import CLIApp

def build_container():
    repo = ProjectRepository()
    service = ToDoService(repo)
    cli_app = CLIApp(service)
    return {"cli_app": cli_app, "service": service, "repo": repo}
