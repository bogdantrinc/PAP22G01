import timeit
import matplotlib.pyplot as plt


def factorial1(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial2(n):
    if n <= 1:
        return 1
    return n * factorial2(n-1)


def time_func1():
    times1 = []
    times2 = []

    for i in range(1, 100):
        times1.append(timeit.timeit(f"factorial1({i})",
                      setup=f"from {__name__} import factorial1",
                      number=100))
    for i in range(1, 100):
        times2.append(timeit.timeit(f"factorial2({i})",
                      setup=f"from {__name__} import factorial2",
                      number=100))
    fig1, (ay1, ay2) = plt.subplots(nrows=2, ncols=1, sharey='all', sharex='all')
    fig1.dpi = 200
    ay1.plot([i for i in range(len(times1))], times1, label="F1")
    ay2.plot([i for i in range(len(times2))], times2, label="F2")
    plt.xlabel('seconds')
    plt.ylabel('km')
    plt.title("My example Graph")
    plt.show()

    return times1, times2


result = time_func1()
print(result[0])
print(result[1])

fig1, (ay1, ay2) = plt.subplots(nrows=2, ncols=1, sharex='all')
