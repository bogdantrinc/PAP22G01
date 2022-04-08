# get timezones with  asyncio
import asyncio
import json
import time

import requests
import aiohttp


async def time_zone_getter(location):
    async with aiohttp.ClientSession() as client:
        result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{location}')
        return json.loads(await result.text())


async def time_getter(city: str):
    async with aiohttp.ClientSession() as client:
        result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{city}')
        print(json.loads(await result.text()))


async def main():
    result = await asyncio.gather(time_zone_getter('europe'),
                                  time_zone_getter('africa'),
                                  time_zone_getter('america'),
                                  time_zone_getter('asia'),
                                  time_zone_getter('australia'))
    # print(result)
    result1 = await asyncio.gather(*tuple([time_getter(i) for i in result[0]]))


start = time.time()
asyncio.run(main())
end = time.time()
print(end-start)