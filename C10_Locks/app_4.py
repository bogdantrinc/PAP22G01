# implement time getters and time zone getter with threads
# - hint use Event and Lock
import json
import time
import requests
from _queue import Empty
from multiprocessing import Process, Queue
from threading import Thread, Event, Lock

cities = Queue()
event = Event()
lock = Lock()

def time_zone_getter(location, cities: Queue, e: Event):
    result = requests.get(url=f'http://worldtimeapi.org/api/timezone/{location}')
    for city in json.loads(result.text):
        cities.put(city)
    e.set()


def time_getter(cities: Queue, e: Event,r: Lock):
    e.wait()
    while r.acquire() and not cities.empty():
        try:
            city = cities.get()
        finally:
            r.release()
        result = requests.get(url=f'http://worldtimeapi.org/api/timezone/{city}')
        print(json.loads(result.text))
    else:
        r.release()

processes = []
for i in range(1):
    thd = Thread(target=time_zone_getter, args=['Europe', cities, event])
    processes.append(thd)

for i in range(1, 6):
    thd = Thread(target=time_getter, args=[cities, event,lock])
    processes.append(thd)

for process in processes:
    process.start()