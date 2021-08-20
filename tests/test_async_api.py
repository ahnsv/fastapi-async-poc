import httpx
import asyncio
import pytest
from app.background import app as background_app


@pytest.mark.asyncio
async def test_background_multiple_requests():
    async with httpx.AsyncClient(app=background_app) as client:
        await asyncio.gather(
            *[
                client.get(f"http://localhost:8000/new_cpu_bound_task/{i}")
                for i in range(10)
            ]
        )
