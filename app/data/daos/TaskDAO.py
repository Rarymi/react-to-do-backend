import uuid
from sqlalchemy.orm import Session

from app.models.Task import Task as ModelTask
from app.data.schemas.Task import Task as SchemaTask


def get_tasks(db: Session):
    return db.query(ModelTask).all()


def create_task(db: Session, task: SchemaTask):
    id = uuid.uuid1()
    db_task = ModelTask(id=id, title=task.title,
                        description=task.description, status=task.status)
    db.add(db_task)
    db.commit()
    return db_task


def update_task(db: Session, task: SchemaTask, task_id: str):
    db.query(ModelTask).filter(
        ModelTask.id == task_id).update(task.dict())
    db.commit()
    return task
