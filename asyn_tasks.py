import asyncio, datetime
import time


# async def what_fun():
#     print("Hello World")
#
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     await what()
#
#
# async def main():
#     task1 = asyncio.create_task(
#         say_after(1, what_fun))
#
#     task2 = asyncio.create_task(
#         say_after(2, what_fun))
#
#     print(f"started at {time.strftime('%X')}")
#
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2
#
#     print(f"finished at {time.strftime('%X')}")
#
#
# asyncio.run(main())
from datetime import datetime
t = datetime.fromtimestamp(1651106100).strftime("%A, %B %d, %Y %I:%M:%S")
print(t)


async def wait_until(dt):
    # sleep until the specified datetime
    now = datetime.datetime.now()
    task = asyncio.sleep((dt - now).total_seconds())
    print(task)
    await task


async def run_at(dt, coro):
    await wait_until(dt)
    return await coro


async def hello():
    print('hello')

loop = asyncio.get_event_loop()
# print hello ten years after this answer was written
loop.create_task(run_at(datetime.datetime(2022, 4, 27, 17, 4), hello()))
loop.run_forever()
