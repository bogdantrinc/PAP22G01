from functools import wraps


def change_type(tip):
    def wrap(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            # Am folosit dict comprehension ca sa modific argumentele de tip key word ale funcției
            return function(*map(tip, args), **{keys: tip(values) for keys, values in kwargs.items()})
        return wrapper
    return wrap

@change_type(str)
def text(*args, **kwargs):
    print("The arguments are: ", list(args) + list(kwargs.values()))


text(0.66, '1', 2, a='3', b=4.99, c=5)
