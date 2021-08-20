import httpx
import asyncio
import pytest
from app.main import app as main_app
from app.background import app as background_app


@pytest.mark.asyncio
async def test_requests():
    async with httpx.AsyncClient(app=main_app) as client:
        r = await client.get("http://localhost:8000/async/1")
        assert r.status_code == 200


@pytest.mark.asyncio
async def test_multiple_requests():
    async with httpx.AsyncClient(app=main_app) as client:
        await asyncio.gather(
            *[client.get(f"http://localhost:8000/async/{i}") for i in range(10)]
        )

@pytest.mark.asyncio
async def test_background_multiple_requests():
    async with httpx.AsyncClient(app=background_app) as client:
        await asyncio.gather(
            *[client.get(f"http://localhost:8000/new_cpu_bound_task/{i}") for i in range(10)]
        )
