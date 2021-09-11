import json
import random
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

slice = on_command('切片', rule=to_me())

@slice.handle()
async def handle_help(bot: Bot, event: Event):
    t_obj = open(r'.\src\assist\title.json', 'r')
    tlist = json.load(t_obj)
    p_obj = open(r'.\src\assist\pic.json', 'r')
    plist = json.load(p_obj)
    u_obj = open(r'.\src\assist\url.json', 'r')
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
    await slice.finish(message=rely)