import time
from multiprocessing import Process, Queue

# VAR1 = ''
#
# def f(name, sleep):
#     time.sleep(sleep)
#     global VAR1
#     print(VAR1, name)
#     VAR1 = 'new value'
#     print(VAR1, name)
#
#
# if __name__ == '__main__':
#     p2 = Process(target=f, args=('lily', 2))
#     p2.start()
#     p2.join()
#     p1 = Process(target=f, args=('bob', 4))
#     p1.start()
#     print(f'all done {VAR1}')
def get_name(VAR1: Queue):
    time.sleep(4)
    val = 'TEST'  # input('Give name:')
    VAR1.put(val)
    print('process1')


def say_hello(VAR1: Queue):
    print('process2')
    time.sleep(1)
    val = VAR1.get(block=True, timeout=2)
    print(f"Hello {val}")
    VAR1.put("ALL DONE")

if __name__ == '__main__':
    VAR1 = Queue()
    p1 = Process(target=get_name, args=(VAR1,))
    p2 = Process(target=say_hello, args=(VAR1,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(VAR1.get())