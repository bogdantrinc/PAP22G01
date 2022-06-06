import time

def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial2(n):
    if n <= 1:
        return 1
    return n * factorial2(n-1)

def time_func():
    times = []
    for i in range(100):
        start = time.time()
        factorial1(1000)
        end = time.time()
        times.append(end - start)
    return times

print(time_func())

import timeit

def time_func1():
    times1 = []
    times2 = []
    for i in range(1, 255):
        times1.append(timeit.timeit(f"factorial1({i})",
                      setup=f"from {__name__} import factorial1",
                      number=1000))
    for i in range(1, 255):
        times2.append(timeit.timeit(f"factorial2({i})",
                      setup=f"from {__name__} import factorial2",
                      number=1000))
    return times1, times2

result = time_func1()
print(result[0])
print(result[1])
