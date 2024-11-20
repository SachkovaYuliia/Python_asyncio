# Завдання 1: Основи асинхронності
# Напишіть асинхронну функцію download_page(url: str), яка симулює завантаження сторінки за допомогою asyncio.sleep(). Функція повинна приймати URL та "завантажувати" сторінку за випадковий проміжок часу від 1 до 5 секунд. Після завершення завантаження, функція повинна вивести повідомлення з URL і часом завантаження.
# Напишіть асинхронну функцію main(urls: list), яка приймає список з декількох URL і завантажує їх одночасно, використовуючи await для паралельного виконання функції download_page().

import asyncio
import random

async def download_page(url: str):
    download_time = random.randint(1, 5)
    await asyncio.sleep(download_time)
    print(f"Сторінка {url} завантажена за {download_time} секунд.")


async def main(urls: list):
    await asyncio.gather(*(download_page(url) for url in urls))

urls = ["https://www.python.org/", "https://edition.cnn.com/", "https://uk.wikipedia.org/", "https://unsplash.com/"]

asyncio.run(main(urls))
