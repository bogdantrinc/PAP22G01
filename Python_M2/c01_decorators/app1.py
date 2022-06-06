# time the execution with a decorator

import time
from datetime import datetime
from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        functie = func(*args, **kwargs)
        end = datetime.now()
        print(f"Execution time: {(end - start).microseconds}")
        return functie

    return wrapper


@decorator
def chr_count(message):
    for _ in message:
        time.sleep(0.1)
    return len(message)


print(chr_count('message'))
