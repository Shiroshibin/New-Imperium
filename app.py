import asyncio

from aiogram import executor
from loader import dp
import handlers

async def function():
    pass

async def on_startup(dispatcher):
    asyncio.create_task(function())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup = on_startup, skip_updates=True)