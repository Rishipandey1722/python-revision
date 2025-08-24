# 📗 Module 4: Async & Concurrency in FastAPI

from fastapi import FastAPI
import time , asyncio

app = FastAPI()


# Normal blocking endpoint

@app.get("/sync/")
def sync_task():
    time.sleep(3)
    return {"message" : "finished sync task after 3 seconds"}

@app.get("/async/")
async def async_task():
    await asyncio.sleep(3)
    return {"message" : "Finished async task after 3 seconds"}



#🔹 2. Running Multiple Tasks in Parallel

@app.get("/parallel/")
async def parallel_task():
    async def task1():
        await asyncio.sleep(3)
        return "task1 done"
    
    async def task2():
        await asyncio.sleep(3)
        return "task2 done"
    
    result = await asyncio.gather(task1(), task2())
    return {"result " : result}