## Quiz
https://www.classmarker.com/

## Homework
Counted List

Create a class for a list like object based on UserList wrapper
https://docs.python.org/3/library/collections.html#collections.UserList

That class should have a method to return a Counter that will count how many objects of each type are present in the 
list. This is actually done directly by counter class below 
https://docs.python.org/3/library/collections.html#collections.Counter

Counter should be updated automatically for at lest 2 list methods (append, pop), so when an object is removed from the 
list or added the counter object is updated.

```python
class Example(UserList):
  ...

x = Example(['1', '2', '3'])
x.get_counter() # returns Counter({'1':1, '2':1 '3':1})
x.append(3)
x.get_counter() # returns Counter({'1':1, '2':1, '3':2})
x.pop(2)
x.get_counter() # returns Counter({'1':1, '3':2})
```