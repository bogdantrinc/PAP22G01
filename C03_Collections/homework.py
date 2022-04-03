r"""
Create a class for a list like object based on UserList wrapper
https://docs.python.org/3/library/collections.html#collections.UserList

That class should have a method to return a Counter that will count how many objects of each type are present in the
list. This is actually done directly by counter class below
https://docs.python.org/3/library/collections.html#collections.Counter

Counter should be updated automatically for at least 2 list methods (append, pop), so when an object is removed from the
list or added the counter object is updated.

class Example(UserList):
  pass

x = Example(['1', '2', '3'])
x.get_counter() # returns Counter({'1':1, '2':1 '3':1})
x.append(3)
x.get_counter() # returns Counter({'1':1, '2':1, '3':2})
x.pop(2)
x.get_counter() # returns Counter({'1':1, '3':2})
"""
from collections import UserList, Counter


class ListaUtilizator(UserList):
    def __init__(self, initlist=None):
        UserList.__init__(self, initlist)
        self.data = []
        if initlist is not None:
            # XXX should this accept an arbitrary sequence?
            if isinstance(initlist, type(self.data)):
                self.data[:] = initlist
            elif isinstance(initlist, UserList):
                self.data[:] = initlist.data[:]
            else:
                self.data = list(initlist)

    def get_counter(self):
        # return Counter([type(obiect) for obiect in self.data])
        return Counter(self.data)

    def append(self, item):
        self.data.append(item)

    def pop(self, i: str = ...):
        self.data.remove(i)


# obiect = ListaUtilizator(['string', 1, 2.0])
obiect = ListaUtilizator(['1', '2', '3'])
print(obiect.get_counter())
obiect.append('3')
print(obiect.get_counter())
obiect.pop('2')
print(obiect.get_counter())
