import asyncio
import time
from pydantic.fields import Field

from pydantic.main import BaseModel
from app.container import Container
from concurrent.futures.process import ProcessPoolExecutor
from typing import Callable, Dict
from contextlib import asynccontextmanager
from dependency_injector.wiring import inject, Provide
from uuid import UUID, uuid4


class Job(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    status: str = "in_progress"
    result: int = None


jobs: Dict[UUID, Job] = {}


@asynccontextmanager
async def async_executor():
    executor = ProcessPoolExecutor()
    try:
        yield executor
    finally:
        executor.shutdown()


async def run_in_process(loop: asyncio.AbstractEventLoop, fn: Callable, *args):
    async with async_executor() as executor:
        return await loop.run_in_executor(executor, fn, *args)


@inject
async def start_cpu_bound_task(
    uid: UUID,
    param: int,
    event_loop: asyncio.AbstractEventLoop = Provide[Container.event_loop],
) -> None:
    jobs[uid].result = await run_in_process(event_loop, fake_cpu_bound_task, param)
    jobs[uid].status = "complete"


def fake_cpu_bound_task(sleep_time: int):
    time.sleep(sleep_time)
    return sleep_time
