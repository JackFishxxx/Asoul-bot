import json
import random
from nonebot import *
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

@on_command('小作文')
async def _(session: CommandSession):
    obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\xzw.json', 'r')
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
    await session.send(message=rely)
