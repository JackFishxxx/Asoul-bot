import json
import random
import os
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

xzw = on_command("小作文", rule=to_me(), priority=5, block=True)

@xzw.handle()
async def _(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])
    
    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'xzw.json')
    with open(data_path, 'rb') as fp:
        xzw_list = json.load(fp)
    
    length = len(xzw_list)
    i = random.randint(0, length-1)
    title = xzw_list[i]
    url = url = r'https://asoul.icu/articles/' + title
    reply = {
        "type": "share",
        "data": {
            "url": url,
            "title": title
            }
        }
    await bot.send_group_msg(group_id=group, message=reply)