from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/async/{number}")
async def get_async(number: int):
    print(f"number: {number}")
    time.sleep(3)
    print("async")
    return "ok"
