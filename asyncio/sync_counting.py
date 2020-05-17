import time


def count_down(name, delay):
    indents = (ord(name) - ord('A')) * '\t'

    n=3
    while n :
        time.sleep(delay)

        duration = time.perf_counter() - start
        print('-' * 40)
        print('%.4f \t%s%s = %i' % (duration, indents, name, n))

        n -= 1

start = time.perf_counter()

count_down('A', 0.5)
count_down('B', 0.3)
count_down('C', 0.1)


print('-' *40)
print('Done')