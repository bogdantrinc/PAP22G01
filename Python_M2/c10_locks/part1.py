import random
import time
from threading import Thread, Lock, RLock

# lock = Lock()
#
# def random_sleep(l: Lock):
#     t = random.randint(1, 3)
#     print("Sleeping: ", t)
#     l.acquire()
#     try:
#         if t == 2:
#             raise ValueError('2 second sleep is not supported')
#         time.sleep(t)
#     finally:
#         # l.release()
#         l.acquire() # this does not work for normal lock
#         l.release()
#     print("Completed sleeping: ", t)
#
# processes = []
# for i in range(5):
#     thd = Thread(target=random_sleep, args=[lock])
#     thd.start()
#     processes.append(thd)

lock = RLock()

def random_sleep(r: Lock):
    t = random.randint(1, 3)
    print("Sleeping: ", t)
    r.acquire()
    try:
        if t == 2:
            raise ValueError('2 second sleep is not supported')
        time.sleep(t)
    finally:
        r.acquire()  # this works for rLock
        r.release()
        print()
        r.release()
    print("Completed sleeping: ", t)

processes = []
for i in range(5):
    thd = Thread(target=random_sleep, args=[lock])
    thd.start()
    processes.append(thd)
