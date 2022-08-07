from hashlib import md5
from nonebot import on_command
import hashlib
import re
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

chance = on_command("概率", rule=to_me(), priority=5, block=True)

@chance.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    usrmsg = str(event.get_message()).split("概率 ")
    group = int(event.get_session_id().split("_")[1])

    if len(usrmsg) == 2:

        usrmsg = usrmsg[1]
        if re.search('我', usrmsg):
            txt = usrmsg + usrid
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
        reply = "[CQ:at,qq={}]\n世界线收束：0.{}\n{}的概率是{}%".format(str(usrid), str(result), str(usrmsg), str(rp))

        await bot.send_group_msg(group_id=group, message=reply)
    else:
        await bot.send_group_msg(group_id=group, message="格式错误，应为：概率 事件")