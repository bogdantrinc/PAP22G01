# Create decorator to increment output with the number of calls
# Create decorate to change all function args to strings.
from functools import wraps
from typing import Union


def change_type(tip):
    def inception(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*map(tip, args), **kwargs)

        return wrapper

    return inception


def increment(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs) + wrapper.calls

    wrapper.calls = 0
    return wrapper


@change_type(str)
@increment
def process_result(number: Union[str, int]):
    if isinstance(number, str):
        return len(number)
    else:
        return number + 1
