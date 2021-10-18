import logging
from typing import List
from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from app.data.daos import TaskDAO
from app.data.schemas import Task
from app.dependencies import get_db

router = APIRouter()
log = logging.getLogger(__name__)


@router.get('/tarefas', response_model=List[Task.GetTask], tags=['tasks'])
async def get_tasks(db: Session = Depends(get_db)):
    return TaskDAO.get_tasks(db)


@router.post('/tarefas', response_model=Task.GetTask, tags=["tasks"])
async def create_task(task: Task.CreateTask, db: Session = Depends(get_db)):
    return TaskDAO.create_task(db, task)


@router.put('/tarefas/{task_id}', response_model=Task.UpdateTask, tags=["tasks"])
async def update_task(task: Task.UpdateTask, task_id: str, db: Session = Depends(get_db)):
    return TaskDAO.update_task(db, task, task_id)
