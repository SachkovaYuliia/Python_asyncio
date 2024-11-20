# Завдання 2: Робота з асинхронними HTTP-запитами
# Використовуючи бібліотеку aiohttp, створіть асинхронну функцію fetch_content(url: str), яка виконує HTTP-запит до вказаного URL і повертає вміст сторінки.
# Створіть асинхронну функцію fetch_all(urls: list), яка приймає список URL і завантажує вміст усіх сторінок паралельно. Використайте await та об'єднання кількох завдань (asyncio.gather()), щоб завантаження всіх сторінок виконувалося одночасно.
# Обробіть можливі помилки запитів, щоб у разі проблеми з підключенням функція повертала відповідне повідомлення про помилку.

import aiohttp
import asyncio

async def fetch_content(url: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.text()  
                else:
                    return f"Помилка: {response.status} для {url}"
    except aiohttp.ClientError as e:
        return f"Помилка підключення до {url}: {e}"

async def fetch_all(urls: list):
    tasks = [fetch_content(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

urls = ["https://www.python.org/", "https://www.pyhton.org/", "https://edition.cnn.com/", "https://uk.wikipedia.org/", "https://unsplash.com/"]

async def main():
    results = await fetch_all(urls)
    for url, content in zip(urls, results):
        print(f"URL: {url}\n Результат:\n{content[:200]}...\n{'-'*60}")

asyncio.run(main())
