from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.models import Task as TaskModel
from app.controllers import TaskController
from app.data.database import engine

TaskModel.Base.metadata.create_all(bind=engine)

origins = ["http://localhost:3000",
           "react-to-do-pu31dlsjb-single-page.vercel.app"]

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=["*"], allow_headers=["*"])
app.include_router(TaskController.router)
