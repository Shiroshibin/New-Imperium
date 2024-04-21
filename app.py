import asyncio
import aioschedule as schedule
from aiogram import executor
from loader import dp
import handlers
from datetime import datetime
from web_app.db import funcs as db_fun



async def wf_lvl_4(data: list):
    print(22222)







async def wf_lvl_3(data:list):
    result = list()
    while len(data) >= 2:
        result.append([[data.pop(0), data.pop(1)]])

    await asyncio.create_task(wf_lvl_4( result))




async def wf_lvl_2(data: list):

    data =[[i for i in data if i[2] == "Онлайн"],
            [i for i in data if i[2] == "Офлайн"],
            [i for i in data if i[2] == "Офис"]]
    
    for item in data:
        await wf_lvl_3(item)



async def wf_lvl_1():
    data = [[i.user_id, i.duration, i.format] for i in db_fun.get_all_applications()]

    data = [[i for i in data if i[1] == "15 мин"],
            [i for i in data if i[1] == "20 мин"],
            [i for i in data if i[1] == "30 мин"]]
    
    tasks = []
    
    for item in data:
        tasks.append(wf_lvl_2(data))
        # await wf_lvl_2(item)
    
    await asyncio.gather(*tasks)

    print(data)


async def function():   
    schedule.every(10).seconds.do(wf_lvl_1)
    while True:
        await asyncio.create_task(schedule.run_pending())
        await asyncio.sleep(10)

    



async def on_startup(dispatcher):
    asyncio.create_task(function())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup = on_startup, skip_updates=True)