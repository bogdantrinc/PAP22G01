# Basic decorators

def area(lenght, width):
    return lenght*width


def decorator(func):
    def wrapper():
        print(f'Calculating result for: {func.__name__}')
        func()
        print('Completed Execution!')
    return wrapper


result = decorator(func=area)
print(type(result))
