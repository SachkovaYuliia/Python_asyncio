# Завдання 6: Завантаження зображень з декількох сайтів
# Уявімо, що ми розробляємо веб-скрапер, який має завантажити зображення з декількох сайтів одночасно. Кожне завантаження зображення - це окрема операція введення-виводу, яка може зайняти певний час.

# Створити асинхронну функцію download_image, яка приймає URL зображення та ім'я файлу для збереження. Вона використовуватиме aiohttp для виконання HTTP-запиту та збереження отриманих даних у файл.

# Головна асинхронна функція main створює список завдань (tasks), кожне з яких відповідає за завантаження одного зображення. Функція asyncio.gather дозволяє запускати всі завдання одночасно і очікувати їх завершення.

import aiohttp
import asyncio
from pathlib import Path

async def download_image(url, filename):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.read()
                    Path(filename).write_bytes(content)
                    print(f"[INFO] Завантажено: {filename}")
                else:
                    print(f"[ERROR] Не вдалося завантажити {url}, статус: {response.status}")
    except Exception as e:
        print(f"[ERROR] Помилка при завантаженні {url}: {e}")

async def main():
    images = [
        ("https://picsum.photos/200/300", "image1.jpg"),
        ("https://picsum.photos/200", "image2.jpg"),
        ("https://picsum.photos/200/300", "image3.jpg"),
        ("https://picsum.photos/200", "image4.jpg"),
    ]

    tasks = [download_image(url, filename) for url, filename in images]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
