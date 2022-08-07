# -*- coding: utf-8 -*-
from nonebot import on_command
import random
import os
import json
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

joke = on_command('冷笑话', aliases={'笑话'}, rule=to_me(), priority=5, block=True)

@joke.handle()
async def _(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'joke.json')
    with open(data_path, 'rb') as fp:
        data = json.load(fp)

    jokes = data["jokes"]
    j = random.randint(0, len(jokes)-1)
    await bot.send_group_msg(group_id=group, message=jokes[j])