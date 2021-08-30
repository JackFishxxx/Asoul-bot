import json
import random
from nonebot import *
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

@on_command('表情包')
async def _(session: CommandSession):
    img_obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\img.json', 'r')
    img_list = json.load(img_obj)
    length = len(img_list)
    i = random.randint(0,length-1)
    rely = {
        "type" : "image",
        "data" : {
            "file" : r'http://' + img_list[i]
        }
    }
    await session.send(message=rely)