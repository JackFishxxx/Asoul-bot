import time
from hashlib import md5
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import re
import os
import json

rp = on_command('人品', aliases={'运势'}, rule=to_me(), priority=5, block=True)
@rp.handle()
async def return_rp(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    usrmsg = str(event.get_message()).split(" ")
    group = int(event.get_session_id().split("_")[1])

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'cp.json')
    with open(data_path,'rb') as fp:
        data = json.load(fp)
    names = data["names"]

    if len(usrmsg) == 1 or (len(usrmsg) == 2 and usrmsg[1] == ""):
        target = usrid
    elif len(usrmsg) == 2:
        target = usrmsg[1]

        #check if it is special name
        for name in names:
            name_list = name.split(",")
            if target in name_list:
                target = name
                break

    t =  time.localtime(time.time())
    rand = t.tm_year + t.tm_yday
    raw = str(rand) + target
    raw = str(raw)
    md5_con = md5(raw.encode('utf8')).hexdigest()
    s = [i for i in md5_con if i.isnumeric()]
    rp = str(int("".join(s))%101)
    if target == usrid:
        target = "你"
    else:
        target = usrmsg[1]
    reply = "[CQ:at,qq={}]{}的运势为：{}".format(str(usrid), str(target), rp)

    if len(usrmsg) == 3:
        reply = "格式错误，应为：运势，或为：运势 对象"
    
    await bot.send_group_msg(group_id=group, message=reply)

