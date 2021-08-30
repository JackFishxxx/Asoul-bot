import json
import random
from nonebot import *
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
#from aiocqhttp.message import MessageSegment

@on_command('切片')
async def _(session: CommandSession):
    t_obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\title.json', 'r')
    tlist = json.load(t_obj)
    p_obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\pic.json', 'r')
    plist = json.load(p_obj)
    u_obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\url.json', 'r')
    ulist = json.load(u_obj)
    length = len(tlist)
    i = random.randint(0,length-1)
    #rely = MessageSegment.share(ulist[i], tlist[i], content=ulist[i], image_url=ulist[i])
    rely = [{
        "type" : "text",
        "data" : {
            "text" : tlist[i] + '\n' + ulist[i] + '\n'
        }
    },
    {
        "type" : "image",
        "data" : {
            "file" : plist[i]
        }
    }
        ]
    await session.send(message=rely)