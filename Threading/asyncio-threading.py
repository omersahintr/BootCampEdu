import threading
import requests as req
import time
import asyncio
import aiohttp


async def get_web_async_wrapper(urls):
    start_time = time.time()
    jason_data = []
    
    async with aiohttp.ClientSession() as session:
        for url in urls:
            async with session.get(url) as resp:
                jason_data.append(await resp.json())


    end_time = time.time()
    dif_time = end_time - start_time
    print(f"Time: {dif_time}")
    return jason_data


urls = ['https://postman-echo.com/delay/2'] * 8 # 8 times request delay 2 seconds

asyncio.run(get_web_async_wrapper(urls))



