# Determine how many times a function was executed
from functools import wraps

def count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count
def function_1():
    print("Running code...")