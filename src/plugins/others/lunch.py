import random
import os
import json
from nonebot.adapters import Bot, Event
from nonebot.plugin import on_keyword
from nonebot.rule import to_me

eat = on_keyword(['午饭', '午餐', '中饭', '晚饭', '晚餐', '夜宵', '中午', '晚上', '半夜', '吃', '恰'], rule=to_me(), priority=5, block=True)

@eat.handle()
async def _(bot: Bot, event: Event):

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'food.json')
    with open(data_path,'rb') as fp:
        data = json.load(fp)
    food = data["food"]
    length = len(food)

    j = random.randint(0, length-1)
    await eat.finish("吃" + food[j] + '！')

breakfast = on_keyword(['早饭', '早餐'], rule=to_me(), priority=4, block=True)
@breakfast.handle()
async def _(bot: Bot, event: Event):
    await breakfast.finish("笑死，带学生还吃早饭？")

bour = on_keyword(['下午茶'], rule=to_me(), priority=4, block=True)
@bour.handle()
async def _(bot: Bot, event: Event):
    await bour.finish("小布尔乔亚行为！把你图图了！")