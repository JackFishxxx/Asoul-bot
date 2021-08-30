import nonebot
from hashlib import md5
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import hashlib
import re

bot = nonebot.get_bot()
@on_command('概率')
async def _(session: CommandSession):
    eve = session.event
    msg = eve['message']
    txt = re.sub(r'\u6982\u7387','',str(msg),count=1)
    txt = txt.strip()
    if txt == '':
        await session.send(message="格式不对啦，请加空格和事件")
    else:
        md5_con = md5(txt.encode('utf8')).hexdigest()
        s = [i for i in md5_con if i.isnumeric()]
        s = "".join(s)
        sha_con = hashlib.sha1(txt.encode('utf8')).hexdigest()
        t = [j for j in sha_con if j.isnumeric()]
        t = "".join(t)
        result = int(s) + int(t)
        rp = result%101
        string = '世界线收束：0.' + str(result) + '\n' + str(txt) + "的概率是" + str(rp) + '%'
        await session.send(message=string)