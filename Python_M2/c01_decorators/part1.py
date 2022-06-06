# Basic decorators

def area(length=10, width=5):
    """ Calculates Area or ractangle """
    return length * width


# print(area())
#
# print(50 * '#')

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f'Calculating result for: {func.__name__}')
#         result = func(*args, **kwargs)
#         print(f"Result is: {result}")
#         print('Completed Execution')
#         return result + 1
#
#     # print(id(wrapper))
#     return wrapper
#
#
# print(area(5, width=3))
# area = decorator(area)
# print(area(5, width=3))
# # result = decorator(func=area)
# # print(result())
# # print(id(result))
# # print(type(result))


# print(50 * '#')
# # delay for debugging
# import time
#
# def delay_with_args(delay_time=10):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(delay_time)
#             result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return delay
#
# print(area(5, width=3))
# area = delay_with_args(delay_time=10)(area)
# print(area(5, width=3))


# Identity of function
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 1
    return wrapper

@decorator
def area(length=10, width=5):
    """ Calculates Area or ractangle """
    return length * width

print(area.__doc__)
print(area.__name__)



