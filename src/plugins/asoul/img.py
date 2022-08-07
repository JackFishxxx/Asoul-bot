import json
import random
import os
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

img = on_command('表情包', rule=to_me(), priority=2, block=True)

@img.handle()
async def _(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])
    
    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'img.json')
    with open(data_path, 'rb') as fp:
        img_list = json.load(fp)

    length = len(img_list)
    i = random.randint(0, length-1)
    reply = {
        "type" : "image",
        "data" : {
            "file" : r'http://' + img_list[i]
        }
    }
    await bot.send_group_msg(group_id=group, message=reply)