import asyncio
import aioschedule
from aiogram import executor
from loader import dp
import handlers
from datetime import datetime

async def work_fun():
    data  = datetime.weekday(datetime.now())
    if data == 7:
        print(data)
    if data == 6:
        print(data)

    print(data)



async def function():
    aioschedule.every().day.at("19:00").do(work_fun)
    while True:
       await aioschedule.run_pending()
       await asyncio.sleep(1)



async def on_startup(dispatcher):
    asyncio.create_task(function())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup = on_startup, skip_updates=True)