import random
import time


def is_prime(number: int):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def primes(limit: int):
    time.sleep(random.randint(1, 3))
    result = []
    for i in range(1, limit + 1):
        if is_prime(i):
            result.append(i)
    return result
