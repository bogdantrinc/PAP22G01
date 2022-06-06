# get timezones with  asyncio
import asyncio
import json
import time
import requests
import aiohttp

zone_data = []


async def time_zone_getter(location):
    async with aiohttp.ClientSession() as client:
        result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{location}')
        zone_data.extend(json.loads(await result.text()))


async def time_getter():
    async with aiohttp.ClientSession() as client:
        while not zone_data:
            await asyncio.sleep(1)
        else:
            city = zone_data.pop()
            result = await client.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/{city}')
            print(json.loads(await result.text()))


async def main():
    result = await asyncio.gather(time_zone_getter('europe'),
                                  time_zone_getter('africa'),
                                  time_zone_getter('america'),
                                  time_zone_getter('asia'),
                                  time_zone_getter('australia'),
                                  time_getter(),
                                  time_getter(),
                                  time_getter())
    # print(result)
    # result1 = await asyncio.gather(*tuple([time_getter(i) for i in zone_data]))


start = time.time()
asyncio.run(main())
end = time.time()
print(end - start)
