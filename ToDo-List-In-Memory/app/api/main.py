from fastapi import FastAPI
from app.api.routers import project_router, task_router
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

def create_app() -> FastAPI:
    app = FastAPI(title="ToDo List API", version="1.0")

    app.include_router(project_router.router)
    app.include_router(task_router.router)

    @app.get("/")
    def root():
        return {"status": "ok", "message": "ToDo List API. See /docs for interactive docs."}

    return app

app = create_app()
