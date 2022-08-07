import json
import random
import os
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

slice = on_command('切片', rule=to_me(), priority=5, block=True)

@slice.handle()
async def handle_help(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])
    
    assist_path = bot.config.assist_path
    title_path = os.path.join(os.getcwd(), assist_path, 'title.json')
    with open(title_path, 'rb') as fp:
        tlist = json.load(fp)
    pic_path = os.path.join(os.getcwd(), assist_path, 'pic.json')
    with open(pic_path, 'rb') as fp:
        plist = json.load(fp)
    url_path = os.path.join(os.getcwd(), assist_path, 'url.json')
    with open(url_path, 'rb') as fp:
        ulist = json.load(fp)

    length = len(tlist)
    i = random.randint(0, length-1)
    reply = [{
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
    await bot.send_group_msg(group_id=group, message=reply)