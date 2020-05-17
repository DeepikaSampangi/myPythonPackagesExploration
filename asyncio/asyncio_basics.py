import asyncio


async def initial_coroutine():
    print("Initial Co routine here")


def main():
    simple_loop = asyncio.get_event_loop()
    simple_loop.run_until_complete(initial_coroutine())
    simple_loop.close()


main()