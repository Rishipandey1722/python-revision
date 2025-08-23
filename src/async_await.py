import time
import asyncio

def task1():
    print("task1 started..")
    time.sleep(2) # blocking
    print("task1 finished..")

def task2():
    print("task2 started...")
    time.sleep(2) #blocking
    print("task2 finished...")

# task1()
# task2()

# here  ouput runs sequentially total 4 seconds..


# now lets see the behavoiur of concurrent execution using async and await...

async def task3():
    print("task3 started ...")
    await asyncio.sleep(2)
    print("task3 finished..")


async def task4():
    print("task4 started...")
    await asyncio.sleep(2)
    print("task4 finished...")

async def main():
    await asyncio.gather(task3(),task4())

asyncio.run(main())