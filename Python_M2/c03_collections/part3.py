from collections import OrderedDict

my_order = OrderedDict()
print(my_order)
x = OrderedDict.fromkeys("abcde")
print(x)
x = OrderedDict.fromkeys((1, "a"))
print(x)
x = OrderedDict({1: {"a":"b"}})
print(x)
print(x.keys())

x["my_key"] = 1234
print(x)
x.popitem()
print(x)

