# Executing only during working hours (9-17)
    # - working hours prints message
    # - outside of working hours function does not execute
    # - decorator must receive working hours as argument
from datetime import datetime
from functools import wraps


def inception(begin=9, end=17):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if datetime.now().hour not in range(begin, end):
                return None
            func(*args, **kwargs)
        return wrapper
    return decorator


@inception(9, 21)
def alarm():
    print("Wake up!")


alarm()
