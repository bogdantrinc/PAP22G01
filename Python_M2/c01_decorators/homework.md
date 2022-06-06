## Quiz
https://www.classmarker.com/ - please create account here and provide in next session

## Homework

1) Create decorator for the following function that will  
 - add line to the opened file containing the numer of times function was called
 - line format "Starting function call: <number>"

2) Create decorator for the following function that will  
 - force all args and kwargs to the type specified as decorator arg 

```python
# @set_type(str)
# @add_line
def open_file(name, mode='r'):
    return open(name, mode)
```
