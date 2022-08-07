import json
import os
import random
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import requests

setu = on_command("色图", aliases={"涩图"}, rule=to_me(), priority=5, block=True)

@setu.handle()
async def return_setu(bot: Bot, event: Event):

    setu_groups = bot.config.setu_groups
    assist_path = bot.config.assist_path
    group = int(event.get_session_id().split("_")[1])

    if group not in setu_groups:
        error = "色图功能在此群未开启，请联系管理员！"
        await bot.send_group_msg(group_id=group, message=error)
    else:
        rand = random.random()
        if rand < 0.5:
            path = os.path.join(os.getcwd(), assist_path, 'jz.png')
            cq = r'[CQ:image,file=file:///'+str(path)+']'
            msg = "请节制\n" + cq

            await bot.send_group_msg(group_id=group, message=msg)
        else:
            url = 'https://api.lolicon.app/setu/v2'

            param = {
                'r18':1,   #添加r18参数 0为否，1为是，2为混合
                'num':1,          #一次返回的结果数量，范围为1到10，不提供 APIKEY 时固定为
            }

            response = requests.get(url, params=param)
            response = response.text
            html = json.loads(response)
            error = html['error']
            data = html['data'][0]
            url = data['urls']['original']
            if error != '':
                error = "出大问题！报错信息：" + error
                await bot.send_group_msg(group_id=group, message=error)
            else:
                cq = r'[CQ:image,file='+str(url)+']'
                await bot.send_group_msg(group_id=group, message=url)

