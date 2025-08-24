from fastapi import FastAPI
import time , asyncio


app = FastAPI()


@app.get("/slow-sync")
def slow_sync_task():
    time.sleep(5)
    return "slow sync task completed"


@app.get("/slow-async")
async def slow_async_task():
    await asyncio.sleep(5)
    return "slow async task completed"

@app.get("/double-task")
async def double_task():

    async def task1():
        await asyncio.sleep(3)
        return "task1 completed"
    
    async def task2():
        await asyncio.sleep(3)
        return "task2 completed"
    
    result = await asyncio.gather(task1() , task2())
    return result


    