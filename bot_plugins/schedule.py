from nonebot import *
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp import MessageSegment
from bilibili_api import user
import re

@on_command('日程表',aliases=('我日程表呢'))
async def _(session: CommandSession):
    u = user.User(703007996)
    page = await u.get_dynamics(0)
    nxt = page['next_offset']
    page2 = await u.get_dynamics(nxt)
    dynamic1 = page['cards']
    dynamic2 = page2['cards']
    dynamic = dynamic1 + dynamic2
    dy_len = len(dynamic)
    for i in range(0,dy_len):
        dy = dynamic[i]
        desc = dy['desc']
        type = desc['type']
        if type != 2:
            pass
        else:
            card = dy['card']
            item = card['item']
            des = item['description']
            des = des.encode('utf-8')
            sche = '日程表'
            sche = sche.encode('utf-8')
            matchobj = re.search(sche, des, re.M|re.I)
            if matchobj:
                pic = item['pictures']
                url = pic[0]['img_src']
                rely = [
                    {
                        "type" : "text",
                        "data" : {
                            "text" : "本周日程表：\n"
                        }
                    },
                    {
                        "type": "image",
                        "data": {
                        "file" : url
                        }
                    }
                ]
                await session.send(message=rely)
                break
            else:
                pass