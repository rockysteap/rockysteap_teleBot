import asyncio
from aiogram import Bot, Dispatcher

from aio_app.handlers import router
from data import keys


async def main():
    bot = Bot(token=keys.MY_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот остановлен')
