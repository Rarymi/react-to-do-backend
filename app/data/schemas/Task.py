from typing import Optional
import typing as t
from pydantic import BaseModel


class Task(BaseModel):

    title: str
    description: Optional[str] = None
    status: str


class CreateTask(Task):
    class Config:
        orm_mode = True


class GetTask(Task):
    id: str

    class Config:
        orm_mode = True


class UpdateTask(Task):
    class Config:
        orm_mode = True
