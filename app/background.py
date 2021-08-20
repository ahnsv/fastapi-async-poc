from uuid import UUID
from app.task import Job, jobs, start_cpu_bound_task
from http import HTTPStatus

from fastapi import APIRouter, BackgroundTasks


router = APIRouter()


@router.post("/new_cpu_bound_task/{param}", status_code=HTTPStatus.ACCEPTED)
async def task_handler(param: int, background_tasks: BackgroundTasks):
    new_task = Job()
    jobs[new_task.uid] = new_task
    background_tasks.add_task(start_cpu_bound_task, new_task.uid, param)
    return new_task


@router.get("/status/{uid}")
async def status_handler(uid: UUID):
    return jobs[uid]
