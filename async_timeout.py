# Завдання 4: Асинхронний таймаут
# Напишіть функцію slow_task(), яка імітує виконання завдання протягом 10 секунд.
# Використовуючи asyncio.wait_for(), викличте slow_task() з таймаутом 5 секунд. Якщо завдання не встигає виконатися за цей час, виведіть повідомлення про перевищення часу очікування.

import asyncio

async def slow_task():
    print("Завдання почалося...")
    await asyncio.sleep(10)  
    print("Завдання завершено.")

async def main():
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Час очікування перевищено!")

asyncio.run(main())
