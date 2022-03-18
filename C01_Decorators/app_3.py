# Determine how many times a function was executed
from functools import wraps

def count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        print(f"Functia a rulat de {wrapper.calls} ori.")
        return result
    wrapper.calls = 0
    return wrapper

@count
def function_1():
    print("Running code...")

function_1()
function_1()