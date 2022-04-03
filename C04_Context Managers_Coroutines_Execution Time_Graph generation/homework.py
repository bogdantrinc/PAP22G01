"""
Create a context manager that will time how long it took to execute the context code block and display a graph with
execution time when the context ends.

- Since the same instance can be used in multiple contexts make sure that the graph will show data for each time the
  object was used in a context. See some usage examples below
- You will need to store the graph in the context object in order to be able to update graph information on each run
- In order to use the same instance and store the graph information the context object is created before we use the
  "with" statement

##### Example #####
class MyMyContextManager:
    def __enter__(self):
    # your code
    def __exit__(self, exc_type, exc_val, exc_tb):
    # your code

obj = MyMyContextManager()
with obj as value1:
    sleep(1)
with obj as value2:
    sleep(2)
with obj as value3:
    sleep(3)

Now graph will contain 3 values based on how long each context needed to execute. Notice that you will not even use
the value 1-3 objects inside the context. You can even choose to write the context as
with obj:
    pass
"""
from time import sleep, time

import matplotlib.pyplot as plt


class MyContextManager:
    def __init__(self):
        self.times_used = 0
        self.ledger = {}

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time()
        self.times_used += 1
        self.ledger[self.times_used] = round(self.end - self.start, 4)
        print(f"{round(self.end - self.start, 4)} secunde")
        plt.dpi = 200
        plt.plot([instance + 1 for instance in range(self.times_used)], [utilizat for utilizat in self.ledger.values()], label="Execution time")
        plt.legend()
        plt.xlabel('Times used')
        plt.ylabel('Seconds')
        plt.title("Timpi de executie")
        plt.show()
        # print(self.ledger)


obj = MyContextManager()
with obj as value1:
    sleep(1)
with obj as value2:
    sleep(9)
with obj as value3:
    sleep(2)
with obj as value4:
    sleep(8)
with obj as value5:
    sleep(3)
with obj as value6:
    sleep(7)
with obj as value7:
    sleep(4)
with obj as value8:
    sleep(6)
with obj as value9:
    sleep(5)
with obj:
    pass
