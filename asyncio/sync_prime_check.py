from math import sqrt
import time

def is_prime(x):
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
    start = time.perf_counter()
    is_prime(9637529763296797)
    is_prime(1231234510496078)
    is_prime(427920331)
    is_prime(157)