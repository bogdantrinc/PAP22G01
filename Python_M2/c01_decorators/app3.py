# determine how many times a function was executed


from functools import wraps


def count(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(wrapper.calls)
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@count
def function1():
    print('Running code')


function1()
function1()
function1()
print(function1.calls)
print(function1.calls)
print(function1.calls)
