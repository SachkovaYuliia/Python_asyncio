# Завдання 7: Порівняння багатопотоковості/багатопроцесорності/асинхронності
# Реалізуйте та дослідіть виконання 500 запитів за допомогою синхронного/багатопотокового/багатопроцесорного/асинхронного режимів за часом.

import time
import requests
import asyncio
import aiohttp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

URL = "https://httpbin.org/delay/1"
REQUESTS_COUNT = 500

def sync_request():
    for _ in range(REQUESTS_COUNT):
        requests.get(URL)

def threaded_request():
    def make_request():
        requests.get(URL)
    
    with ThreadPoolExecutor() as executor:
        executor.map(make_request, range(REQUESTS_COUNT))

def multiprocess_request():
    def make_request(_):
        requests.get(URL)
    
    with ProcessPoolExecutor() as executor:
        executor.map(make_request, range(REQUESTS_COUNT))

async def async_request():
    async def fetch(session):
        async with session.get(URL) as response:
            await response.text()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session) for _ in range(REQUESTS_COUNT)]
        await asyncio.gather(*tasks)

def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    print(f"{func.__name__}: {end_time - start_time:.2f} секунд")

def measure_time_async(coro, *args):
    start_time = time.time()
    asyncio.run(coro(*args))
    end_time = time.time()
    print(f"{coro.__name__}: {end_time - start_time:.2f} секунд")

if __name__ == "__main__":
    print("Порівняння продуктивності:")
    
    measure_time(sync_request)
    
    measure_time(threaded_request)

    measure_time(multiprocess_request)
    
    measure_time_async(async_request)
