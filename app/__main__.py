if __name__ == "__main__":
    from app.container import Container
    from app.background import router
    from app import task
    import uvicorn

    container = Container()
    container.wire([task])
    app = container.app()
    app.include_router(router=router)
    uvicorn.run(app)
