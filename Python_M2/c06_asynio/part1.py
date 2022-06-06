import json

import requests
import aiohttp
import asyncio


# async def f():
#     print('hello')
#     await asyncio.sleep(1)
#     print('world')
#
#
# async def g():
#     print('hello1')
#     await asyncio.sleep(2)
#     print('world2')
#
#
# async def main():
#     task = await asyncio.gather(f(), g())
#
#
# asyncio.run(main())
#
#
# async def get_address(client, url):
#     result = await client.request(method='GET', url=url)
#     return result
#
#
# async def get_time():
#     async with aiohttp.ClientSession() as client:
#         result = await asyncio.gather(get_address(client, 'https://www.google.com'),
#                                       get_address(client, 'https://www.yahoo.com'))
#
#         print(result)
#
#
# asyncio.run(get_time())

result = requests.get('http://worldtimeapi.org/api/timezone')
print(json.loads(result.text))