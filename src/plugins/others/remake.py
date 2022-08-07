# -*- coding: utf-8 -*-
import json
import random
import os
from nonebot.plugin import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

remake = on_command("remake", aliases={"重开"}, rule=to_me(), priority=5)

@remake.handle()
async def _(bot: Bot, event: Event):
    
    usrid = str(event.get_user_id())
    group = int(event.get_session_id().split("_")[1])

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'remake.json')
    with open(data_path,'rb') as fp:
        data = json.load(fp)
    re_list = data["re_list"]

    ran = random.random()
    length = len(re_list)
    j = random.randint(0, length-1)

    reply = "[CQ:at,qq={}]\n世界线变动：{}\n重生之你是{}".format(str(usrid), str(ran), re_list[j])

    await bot.send_group_msg(group_id=group, message=reply)
