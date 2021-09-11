from typing import Text
import nonebot
from hashlib import md5
from nonebot import on_command
import hashlib
import re
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

chance = on_command("概率", rule=to_me(), priority=5)

@chance.handle()
async def _(bot: Bot, event: Event):
    usrname = event.get_user_id()
    usrmsg = str(event.get_message()).replace('概率','').replace(' ','')

    if usrmsg != '':

        if re.search('我', usrmsg):
            txt = usrmsg + usrname
            usrmsg = usrmsg.replace("我", "&").replace("你", "我").replace("&", "你")
        elif re.search('你', usrmsg):
            txt = usrmsg + 'bot'
            usrmsg = usrmsg.replace("你", "我")
        else:
            txt = usrmsg

        md5_con = md5(txt.encode('utf8')).hexdigest()
        s = [i for i in md5_con if i.isnumeric()]
        s = "".join(s)
        sha_con = hashlib.sha1(txt.encode('utf8')).hexdigest()
        t = [j for j in sha_con if j.isnumeric()]
        t = "".join(t)
        result = int(s) + int(t)
        rp = result%101

        rely = [{
            "type": "at",
            "data": {
                "qq": usrname,
                "name": ""
            }
        },
        {
            "type": "text",
            "data": {
                "text": "\n" + '世界线收束：0.' + str(result) + '\n' + str(usrmsg) + "的概率是" + str(rp) + '%'
            }
        }
        ]

        await chance.send(message=rely)
    else:
        await chance.reject(message="格式不对啦，请加空格和事件")