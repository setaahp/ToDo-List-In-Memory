from app.db.session import SessionLocal
from app.services.project_service import ProjectServiceDB
from app.services.task_service import TaskServiceDB
from app.cli.cli_app import CLIApp
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

db = SessionLocal()
project_service = ProjectServiceDB(db)
task_service = TaskServiceDB(db)
cli_app = CLIApp(project_service, task_service)

if __name__ == "__main__":
    cli_app.run()
