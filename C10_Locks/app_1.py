import os
from threading import Thread, Lock


lock = Lock()
servers = ['8.8.8.8', '8.8.4.4.', '142.250.187.132']
# ping these servers in parallel but only 1 IO can happen at a time


def ping(l: Lock, ip):
    l.acquire()
    try:
        response = os.system("ping " + ip)
    finally:
        l.release()
    return response


processes = []
for ip in servers:
    thd = Thread(target=ping, args=[lock, ip])
    thd.start()
    processes.append(thd)
    thd.join()
