def calculate_area(length, high):
    if type(length) != int:
        raise TypeError
    return length * high

print(calculate_area(2, '3'))