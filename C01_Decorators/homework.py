"""
1) Create decorator for the following function that will
 - add line to the opened file containing the numer of times function was called
 - line format "Starting function call: <number>"

2) Create decorator for the following function that will
 - force all args and kwargs to the type specified as decorator arg

    #@set_type(str)
    #@add_line
    def open_file(name, mode='r'):
        return open(name, mode)
 """

from functools import wraps

# def set_type(tip):
#     """
#     Forces all args and kwargs to the type specified as decorator arg.
#     """
#     def wrap(function):
#         @wraps(function)
#         def wrapper(*args, **kwargs):
#             return function(*map(tip, args), **{keys: tip(values) for keys, values in kwargs.items()})
#         return wrapper
#     return wrap

def add_line(function):
    """
    Appends a new line to the file, stating the number of calls for this function (including the current call).
    """
    @wraps(function)
    def wrapper(name, mode):
        wrapper.calls += 1
        with open(name, 'a') as f:
            f.write(f"\nStarting function call: {wrapper.calls}")
        return function(name, mode)
    wrapper.calls = 0
    return wrapper

#@set_type(str)
@add_line
def open_file(name, mode='r'):
    """
    Opens a file.
    """
    return open(name, mode)


if __name__ == "__main__":
    print("Fisierul original este: ")
    print("".center(50, '-'))
    with open('homework.txt', 'r') as f:
        print(f.read())
    print("".center(50, '-'))
    ####################################################
    # Modificam fisierul apeland functia in modul append
    f = open_file("homework.txt", "a")
    f.write("\nTHIS IS ANOTHER SAMPLE!")
    f.close()
    # Apelam functia in modul read
    open_file('homework.txt', 'r')
    ####################################################
    print("\n\n\nFisierul modificat este: ")
    print("".center(50, '-'))
    with open('homework.txt', 'r') as f:
        print(f.read())
    print("".center(50, '-'))