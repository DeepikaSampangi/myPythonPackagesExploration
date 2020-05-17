import asyncio
from math import sqrt
import time

async def is_prime(x):
    duration = time.perf_counter() - start
    print("%.4f" %(duration))

    print(f'Processing {x}')

    if x < 2 or x%2 == 0:
        print(f"{x} is not a prime no.")

    else:
        limit = int(sqrt(x)) + 1
        for i in range(3, limit, 2):
            if x % i == 0:
                print(f"{x} is not a prime no.")
                return

        print(f"{x} is a prime no.")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start = time.perf_counter()
    tasks = [
        loop.create_task(is_prime(9637529763296797)),
        loop.create_task(is_prime(1231234510496078)),
        loop.create_task(is_prime(427920331)),
        loop.create_task(is_prime(157)),
    ]

    loop.run_until_complete(asyncio.wait(tasks))
