# app/api/routers/tasks.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.api import dependencies
from app.api.schemas import schemas
from app.api.dependencies import get_db
from app.services.task_service import TaskServiceDB

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=schemas.TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: schemas.TaskCreate, db: Session = Depends(get_db)):
    svc = TaskServiceDB(db)
    task = svc.create_task(payload.dict())
    return task

@router.get("/", response_model=List[schemas.TaskOut])
def list_tasks(project_id: int = Query(None), db: Session = Depends(get_db)):
    svc = TaskServiceDB(db)
    if project_id:
        return svc.list_tasks_by_project(project_id)
    return svc.list_tasks()

@router.get("/{task_id}", response_model=schemas.TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    svc = TaskServiceDB(db)
    t = svc.get_task(task_id)
    if not t:
        raise HTTPException(status_code=404, detail="Task not found")
    return t

@router.put("/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, payload: schemas.TaskUpdate, db: Session = Depends(get_db)):
    svc = TaskServiceDB(db)
    updated = svc.update_task(task_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    svc = TaskServiceDB(db)
    success = svc.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None
