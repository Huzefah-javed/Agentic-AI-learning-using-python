import requests
import asyncio

async def fetchData():
    print("start 1....")
    await asyncio.sleep(4)
    print("Complete 1....")
async def fetchData2():
    print("start 2....")
    await asyncio.sleep(4)
    print("Complete 2....")

async def main() -> None:
    t=asyncio.create_task(fetchData())
    t2=asyncio.create_task(fetchData2())
    await t
    await t2

asyncio.run(main())