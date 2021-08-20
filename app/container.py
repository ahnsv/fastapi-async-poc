import asyncio
from dependency_injector import containers, providers
from fastapi.applications import FastAPI


class Container(containers.DeclarativeContainer):
    event_loop = providers.Resource(asyncio.get_event_loop)
    app = providers.Factory(FastAPI)
