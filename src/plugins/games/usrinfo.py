from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import json
import os

usrinfo = on_command('用户面板', aliases={'个人信息'}, rule=to_me(), priority=5, block=True)

@usrinfo.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    path = './src/data/users/{}.json'.format(usrid)
    group = int(event.get_session_id().split("_")[1])
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as json_file:
            usr = json.load(json_file)
            titles = usr['titles']
            money = usr['usrinfo']['money']
            talents = usr['talents']
            goods = usr['goods']

            talent_line = ''
            for talent in talents:
                talent_line = talent_line + talent + '  '
            if talent_line == '':
                talent_line = '无'

            title_line = ''
            for title in titles:
                title_line = title_line + title + '  '
            
            good_line = ''
            for good, num in goods.items():
                good_line = good_line + good + 'x' + str(num) + '  '
            if good_line == '':
                good_line = '无'
            
            

            reply = [{
                "type": "at",
                "data": {
                    "qq": usrid,
                    "name": ""
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "\n金钱：{}元".format(money)
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "\n物品：{}".format(good_line)
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "\n称号：{}".format(title_line)
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "\n天赋：{}".format(talent_line)
                }
            }
            ]
            await bot.send_group_msg(group_id=group, message=reply)
    else:
        reply = '[CQ:at,qq='+str(usrid)+']您还未注册！'
        await bot.send_group_msg(group_id=group, message=reply)