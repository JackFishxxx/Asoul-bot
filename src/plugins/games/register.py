import re
from nonebot import on_command, on_regex
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import json
import os
from nonebot.matcher import Matcher
from nonebot.adapters import Message

register = on_command('注册', rule=to_me(), priority=5, block=True)

@register.handle()
async def _(bot: Bot, event: Event, matcher: Matcher):

    usrid = str(event.get_user_id())
    msg = str(event.get_message())
    group = int(event.get_session_id().split("_")[1])
    names = os.listdir(r'./src/data/users')
    name = usrid + '.json'

    if name not in names:

        info = re.findall(r'([1-9][0-9]*)', msg)
        print(info)
        if len(info) != 8:
            await bot.send_group_msg(group_id=group, message="请按照说明重新填写！")
        for i in info:
            if int(i) <= 0 or int(i) > 10:
                await bot.send_group_msg(group_id=group, message="请按照说明重新填写！")
        usr = {
            "个人信息":{
                "姓名": usrid,
                "等级": 1,
                "金钱": 100,
                "经验": 0
            },
            "属性":{
                "力量": int(info[0]),
                "体质": int(info[1]),
                "精神": int(info[2]),
                "智力": int(info[3]),
                "准确": int(info[4]),
                "敏捷": int(info[5]),
                "外貌": int(info[6]),
                "意志": int(info[7]),
                "行动点数": 10
            },
            "goods":{
                "身份证": 1
            },
            "talents":{

            },
            "titles":[
                '小白',
                '封弊者'
            ]
        }
        path = './src/data/users/{}.json'.format(usrid)
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(usr, json_file)

        reply = '[CQ:at,qq='+str(usrid)+']注册成功！'
        await bot.send_group_msg(group_id=group, message=reply)
    
    else:
        reply = '[CQ:at,qq='+str(usrid)+']账号已存在！'
        await bot.send_group_msg(group_id=group, message=reply)

