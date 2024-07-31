from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

import asyncio

from app.handlers import router


async def main():
    bot = Bot(token='6042893266:AAF9Zb5S8TPFHYPeY5tOQjA7p3WV1fPEYMY')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')


