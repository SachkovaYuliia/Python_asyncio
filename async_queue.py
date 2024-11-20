# Завдання 3: Асинхронні черги
# Реалізуйте асинхронну чергу завдань за допомогою asyncio.Queue. Створіть функцію producer(queue), яка додає 5 завдань до черги із затримкою в 1 секунду.
# Напишіть функцію consumer(queue), яка забирає завдання з черги, виконує його (наприклад, виводить повідомлення), імітуючи роботу з кожним завданням із затримкою в 2 секунди.
# Створіть функцію main(), яка одночасно запускає і producer, і кілька споживачів (consumer) за допомогою asyncio.gather(), щоб споживачі обробляли завдання в міру їх появи в черзі.

import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)  
        task = f"Завдання {i + 1}"
        await queue.put(task)  
        print(f"[Producer] Додано: {task}")

async def consumer(queue, consumer_id):
    while True:
        task = await queue.get()  
        if task is None:
            print(f"[Consumer {consumer_id}] Завдання не виконуються")
            queue.task_done()
            break
        print(f"[Consumer {consumer_id}] Отримано: {task}")
        await asyncio.sleep(2)  
        print(f"[Consumer {consumer_id}] Завершено: {task}")
        queue.task_done()  

async def main():
    queue = asyncio.Queue()  

    producers = [producer(queue)]
    consumers = [consumer(queue, i + 1) for i in range(3)]  

    await asyncio.gather(
        *producers,
        asyncio.create_task(queue.join()),  
        return_exceptions=True  
    )

    for _ in consumers:
        await queue.put(None)  
    await asyncio.gather(*consumers, return_exceptions=True)

asyncio.run(main())
