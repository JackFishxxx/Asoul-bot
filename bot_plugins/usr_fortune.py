from nonebot import *
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp import MessageSegment
import time
from hashlib import md5



@on_command('今日人品',aliases=('今日运势','运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    usrqq = str(session.ctx['user_id'])
    usrqq = int(usrqq)
    rp = usrqq + t
    rp = str(rp)
    md5_con = md5(rp.encode('utf8')).hexdigest()
    s = [i for i in md5_con if i.isnumeric()]
    s = "".join(s)
    s = int(s)
    rp = s%101
    rp = str(rp)
    rely = [{
        "type": "at",
        "data": {
            "qq": usrqq,
            "name": ""
        }
    },
    {
            "type": "text",
            "data": {
                "text": "的运势为："
            }
    },
    {
            "type": "text",
            "data": {
                "text": rp
            }
    }
    ]
    await session.send(message=rely)