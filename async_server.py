# Завдання 5: Створення простого асинхронного веб-сервера
# 1. Використовуючи бібліотеку aiohttp, створіть простий асинхронний веб-сервер, який має два маршрути:

# /, який повертає простий текст "Hello, World!".
# /slow, який симулює довгу операцію з затримкою в 5 секунд і повертає текст "Operation completed".
# 2. Запустіть сервер і перевірте, що він може обробляти кілька запитів одночасно (зокрема, маршрут /slow не блокує інші запити).

from aiohttp import web
import asyncio

async def handle_root(request):
    return web.Response(text="Hello, World!")

async def handle_slow(request):
    await asyncio.sleep(5)  
    return web.Response(text="Operation completed")

def create_app():
    app = web.Application()
    app.router.add_get("/", handle_root)  
    app.router.add_get("/slow", handle_slow)  
    return app

if __name__ == "__main__":
    web.run_app(create_app(), host="127.0.0.1", port=8080)
