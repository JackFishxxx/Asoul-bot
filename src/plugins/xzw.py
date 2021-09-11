import json
import random
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

xzw = on_command("小作文", rule=to_me(), priority=5)

@xzw.handle()
async def return_xzw(bot: Bot, event: Event):

    ret_xzw = await get_xzw()
    await xzw.finish(ret_xzw)


async def get_xzw():

    obj = open(r'.\src\assist\xzw.json', 'r')  #from the root of the project not the current file
    xzw_list = json.load(obj)
    length = len(xzw_list)
    i = random.randint(0,length-1)
    title = xzw_list[i]
    url = url = r'https://asoul.icu/articles/' + title
    rely = {
        "type": "share",
        "data": {
            "url": url,
            "title": title
            }
        }
    return rely