from app.db.session import SessionLocal
from app.services.project_service import ProjectServiceDB
from app.services.task_service import TaskServiceDB
from app.cli.cli_app import CLIApp
from app.db.base import Base
from app.db.session import engine
import warnings
import sys

Base.metadata.create_all(bind=engine)

db = SessionLocal()
project_service = ProjectServiceDB(db)
task_service = TaskServiceDB(db)
cli_app = CLIApp(project_service, task_service)

if __name__ == "__main__":

    warnings.warn(
    "\n\n⚠️ CLI is deprecated and will be removed in a future release.\n "
    "Please use the FastAPI endpoints at http://127.0.0.1:8000/docs instead.",
    DeprecationWarning
)

    if len(sys.argv) > 1 and sys.argv[1] == "api":
        import uvicorn
        uvicorn.run("app.api.main:app", host="127.0.0.1", port=8000, reload=True)
    else:
        cli_app.run()
