# -*- coding: utf-8 -*-
from nonebot.rule import to_me
import requests
import json
import time
from nonebot.adapters import Bot, Event
from nonebot import on_command

fan_num = on_command('实时粉丝数',aliases={'粉丝数'}, rule=to_me())

@fan_num.handle()
async def _(bot: Bot, event: Event):
    uid = [672346917,672353429,351609538,672328094,672342685,703007996,434334701]
    name = ["向晚","贝拉","珈乐","嘉然","乃琳","Asoul_official","七海Nana7mi"]
    payload = "注意！此功能不应经常使用！\n"
    i = 0
    for uid_u in uid:
        try:
            bilibili_api = requests.get("http://api.bilibili.com/x/relation/stat?vmid={}".format(uid_u))  # 访问网址，数据存到变量
        except OSError:
            break
        extracting_json = bilibili_api.text
        python_dictionary = json.loads(extracting_json)
        try:
            fans_num = python_dictionary['data']['follower']
        except TypeError:
            break
        payload = payload + name[i] + ":" + str(fans_num) + "\n"
        i = i + 1
        time.sleep(0.5)
    await fan_num.finish(payload)

