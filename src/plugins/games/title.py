from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import json
import os

all_title = on_command('显示所有称号', aliases={'显示全部称号', '展示所有称号', '展示全部称号'}, rule=to_me(), priority=5, block=True)

@all_title.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    path = './src/data/users/{}.json'.format(usrid)
    group = int(event.get_session_id().split("_")[1])
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as json_file:
            usr = json.load(json_file)
        titles = usr['titles']
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
                    "text": "你的称号有：\n"
                }
        }
        ]
        for title in titles[::-1]:
            reply.insert(2,{
                    "type": "text",
                    "data": {
                        "text": title + "\n"
                    }
            }
            )
        await bot.send_group_msg(group_id=group, message=reply)
    else:
        reply = '[CQ:at,qq='+str(usrid)+']您还未注册！'
        await bot.send_group_msg(group_id=group, message=reply)



change_title = on_command('修改显示称号', aliases={'修改展示称号'}, rule=to_me(), priority=5, block=True)

@change_title.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    usrmsg = str(event.get_message())
    path = './src/data/users/{}.json'.format(usrid)
    group = int(event.get_session_id().split("_")[1])
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as json_file:
            usr = json.load(json_file)
        titles = usr['titles']
        if usrmsg in titles:
            titles.remove(usrmsg)
            titles.insert(0, usrmsg)
            usr['titles'] = titles
            with open(path, 'w', encoding='utf-8') as json_file:
                json.dump(usr, json_file)
        else:
            reply = '[CQ:at,qq='+str(usrid)+']你没有该称号！'
            await bot.send_group_msg(group_id=group, message=reply)

        reply = '[CQ:at,qq='+str(usrid)+']修改成功！'
        await bot.send_group_msg(group_id=group, message=reply)
    else:
        reply = '[CQ:at,qq='+str(usrid)+']您还未注册！'
        await bot.send_group_msg(group_id=group, message=reply)

show_title = on_command('展示称号', aliases={'显示称号'}, rule=to_me(), priority=5, block=True)

@show_title.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    path = './src/data/users/{}.json'.format(usrid)
    group = int(event.get_session_id().split("_")[1])
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as json_file:
            usr = json.load(json_file)
            title = usr['titles'][0]  #所有称号的第一个为展示称号
            reply = '[CQ:at,qq='+str(usrid)+']你的称号是：【'+str(title)+'】\n'
            await bot.send_group_msg(group_id=group, message=reply)
    else:
        reply = '[CQ:at,qq='+str(usrid)+']您还未注册！'
        await bot.send_group_msg(group_id=group, message=reply)