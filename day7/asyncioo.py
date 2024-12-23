import asyncio

async def func():
    task=asyncio.create_task(func1())
    print("One")
    await asyncio.sleep(1)
    print("three")
    await asyncio.sleep(1)
    # await func1()
    # await asyncio.sleep(1)
    print("five")
    await asyncio.sleep(1)
    print("six")

async def func1():
    print("two")
    await asyncio.sleep(1)
    print("four")

asyncio.run(func())