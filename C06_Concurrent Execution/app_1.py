import asyncio
import json
import time

import aiohttp
import requests

# result = requests.get('http://worldtimeapi.org/api/timezone')
# print(json.loads(result.text))

async def time_zone_getter(location):
    async with aiohttp.ClientSession() as client:
        result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{location}')
        print(json.loads(await result.text()))
start = time.time()
asyncio.run(time_zone_getter('europe'))
stop = time.time()
print("Time: ", stop-start)