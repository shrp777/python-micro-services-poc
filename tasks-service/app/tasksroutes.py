from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID
from fastapi import APIRouter

router = APIRouter()


class Task(BaseModel):
    id: UUID
    user_id: int
    content: str
    created_at: datetime = None
    completed: bool = False
    completed_at: datetime = None


fake_db: List[Task] = []


@router.get("/tasks", response_model=List[Task])
def get_articles():
    return fake_db


@router.get("/tasks/{task_id}", response_model=Task)
def get_article(task_id: UUID):
    for task in fake_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task doest not exist")


@router.post("/tasks", response_model=Task)
def create_article(task: Task):
    fake_db.append(task)
    return task


@router.put("/tasks/{task_id}", response_model=Task)
def update_article(task_id: UUID, updated_article: Task):
    for id, task in enumerate(fake_db):
        if task.id == task_id:
            fake_db[id] = updated_article
            return updated_article
    raise HTTPException(status_code=404, detail="Task doest not exist")


@router.delete("/tasks/{task_id}", response_model=dict)
def delete_article(task_id: UUID):
    for id, task in enumerate(fake_db):
        if task.id == task_id:
            del fake_db[id]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task doest not exist")
