from multiprocessing import Process
import json
import time
import requests

def time_zone_getter(location):
    result = requests.get(url=f'http://worldtimeapi.org/api/timezone/{location}')
    print(json.loads(result.text))


if __name__=='__main__':
    processes = []
    for location in ['europe', 'asia', 'america']:
        p = Process(target=time_zone_getter, args=(location,))
        processes.append(p)
    # p1 = Process(target=time_zone_getter, args=('europe',))
    start = time.time()
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    # p1.start()
    # p1.join()
    stop = time.time()
    print("Time: ", stop - start)