from _queue import Empty
from multiprocessing import Process, Queue
import json
import time
import requests
import aiohttp


def time_zone_getter(location, cities: Queue):
    result = requests.get(url=f'http://worldtimeapi.org/api/timezone/{location}')
    # print(json.loads(result.text))
    for city in json.loads(result.text):
        cities.put(city)

def time_getter(cities: Queue):
    while True:
        try:
            city=cities.get(timeout=10)
        except Empty:
            print("We're done.")
            break
        print(city)
        result = requests.get(url=f'http://worldtimeapi.org/api/timezone/{city}')
        print(json.loads(result.text))



if __name__ == "__main__":
    processes = []
    cities = Queue()
    for location in ['europe', 'asia', 'america']:
        p = Process(target=time_zone_getter, args=(location, cities))
        processes.append(p)
    start = time.time()
    for process in processes:
        process.start()
    for i in range(3):
        p = Process(target=time_getter, args=(cities,))
        p.start()
    for process in processes:
        process.join()
    # p1.start()
    # p1.join()
    stop = time.time()
    print('Time: ', stop-start)
    # while not cities.empty():
    #     print(cities.get())
    # print(cities.get())
    # print(cities.empty())
    # print(cities.get())
    # print(cities.empty())
    # print(cities.get())
    # print(cities.empty())
    print(cities.qsize())
    # for i in range(cities.qsize()):
    #     p = Process(target=time_getter, args=(cities,))
    #     p.start()