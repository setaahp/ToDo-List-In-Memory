# app/api/routers/projects.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.api import dependencies
from app.api.schemas import schemas
from app.api.dependencies import get_db
from app.services.project_service import ProjectServiceDB

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/", response_model=schemas.ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(payload: schemas.ProjectCreate, db: Session = Depends(get_db)):
    svc = ProjectServiceDB(db)
    project = svc.create_project(payload.title, payload.description)
    return project

@router.get("/", response_model=List[schemas.ProjectOut])
def list_projects(db: Session = Depends(dependencies.get_db)):
    svc = ProjectServiceDB(db)
    return svc.list_projects()

@router.get("/{project_id}", response_model=schemas.ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db)):
    svc = ProjectServiceDB(db)
    proj = svc.get_project(project_id)
    if not proj:
        raise HTTPException(status_code=404, detail="Project not found")
    return proj

@router.put("/{project_id}", response_model=schemas.ProjectOut)
def update_project(project_id: int, payload: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    svc = ProjectServiceDB(db)
    updated = svc.update_project(project_id, payload.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated

@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    svc = ProjectServiceDB(db)
    success = svc.delete_project(project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return None
