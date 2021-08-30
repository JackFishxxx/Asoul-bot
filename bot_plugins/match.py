import nonebot
from hashlib import md5
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import hashlib
import re

bot = nonebot.get_bot()
@on_command('匹配')
async def _(session: CommandSession):
    eve = session.event
    sender = eve['sender']
    usr_id = sender['user_id']
    msg = eve['message']
    txt = re.sub(r'\u5339\u914d','',str(msg),count=1)
    txt = txt.strip()
    if txt == '':
        await session.send(message="格式不对啦，请加空格和匹配对象")
    else:
        md5_con = md5(txt.encode('utf8')).hexdigest()
        s = [i for i in md5_con if i.isnumeric()]
        s = "".join(s)
        sha_con = hashlib.sha1(txt.encode('utf8')).hexdigest()
        t = [j for j in sha_con if j.isnumeric()]
        t = "".join(t)
        result = int(s) + int(t)
        rp = (result + usr_id)%101
        string = "嗨呀，你和" + str(txt) + "的相配程度竟然是" + str(rp) + '%呀！'
        await session.send(message=string)