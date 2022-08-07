from hashlib import md5
from nonebot import on_command
import hashlib
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

def get_result(txt):
    md5_con = md5(txt.encode('utf8')).hexdigest()
    s = [i for i in md5_con if i.isnumeric()]
    s = "".join(s)
    sha_con = hashlib.sha1(txt.encode('utf8')).hexdigest()
    t = [j for j in sha_con if j.isnumeric()]
    t = "".join(t)
    result = (int(s) + int(t))%101

    return result

remake = on_command('匹配', rule=to_me(), priority=5)

@remake.handle()
async def _(bot: Bot, event: Event):

    usrname = event.get_user_id()
    usrmsg = str(event.get_message()).split(" ")
    group = int(event.get_session_id().split("_")[1])

    if len(usrmsg) == 2 and usrmsg[1] != " ":
        txt = usrname + usrmsg[1]
        result = get_result(txt)
        reply = "[CQ:at,qq={}]\n嗨呀，你和{}的相配程度竟然是{}%呀！".format(str(usrname), str(usrmsg[1]), str(result))

    elif len(usrmsg) == 3 and usrmsg[1] != " " and usrmsg[2] != " ":
        txt = usrmsg[1] + usrmsg[2]
        result = get_result(txt)
        reply = "[CQ:at,qq={}]\n嗨呀，{}和{}的相配程度竟然是{}%呀！".format(str(usrname), str(usrmsg[1]), str(usrmsg[2]), str(result))
    
    else:
        reply ="格式错误，应为：匹配 A，或为：匹配 A B"
        
    await bot.send_group_msg(group_id=group, message=reply)