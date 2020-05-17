import asyncio
import random


async def initial_coroutine():
    process_time = random.randint(1, 10)
    print("Initial Co routine here")


# @asyncio.corotuine
# def other_way_of_calling():
#     print("Another way of calling a async coroutine, with annotions")


async def random_int(id):
    process_time = random.randint(1,10)
    await asyncio.sleep(process_time)
    print(f"Coroutine: {id}, has successfully completed after {process_time} seconds")

async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(random_int(i)))

    await asyncio.gather(*tasks)

simple_loop = asyncio.get_event_loop()
simple_loop.run_until_complete(main())
simple_loop.close()
