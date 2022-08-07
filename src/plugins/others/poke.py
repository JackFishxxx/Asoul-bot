import os
from nonebot.plugin import on_notice
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import PokeNotifyEvent
import random

async def _poke(bot: Bot, event: Event) -> bool:
    return (
        isinstance(event, PokeNotifyEvent)
        and event.is_tome()
    )

poke = on_notice(_poke, priority=5, block=True)

@poke.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    group = int(event.get_session_id().split("_")[1])

    usr_stat = await bot.get_group_member_info(group_id=group, user_id=usrid)
    usr_is_admin = usr_stat["role"]
    bot_stat = await bot.get_group_member_info(group_id=group, user_id=event.self_id)
    bot_is_admin = bot_stat["role"]

    coin_path = os.path.join(os.getcwd(), bot.config.assist_path, "coin.jpg")
    rand = random.random()
    if usr_is_admin != "member":
        if rand < 0.2:
            reply = "别戳了，再戳烦了！"
        elif rand >= 0.2 and rand < 0.5:
            reply = "你戳你🐎呢？"
        elif rand >= 0.5 and rand < 0.8:
            reply = "是管理还戳？我真怀疑有人闲的程度啊！"
        else:
            cq = r'[CQ:image,file=file:///'+str(coin_path)+']'
            reply = "哇哇哇哇！！！💃💃💃爆金币了happy！！！\n"+ cq
    elif usr_is_admin == "member" and bot_is_admin != "member":
        if rand < 0.3:
            reply = "别戳了，再戳烦了！"
            dure = 0
        elif rand >= 0.3 and rand < 0.7:
            reply = "蓝天白云..."
            dure = (random.random()+1) * 10 * 60
        elif rand >= 0.7 and rand < 0.89:
            reply = "哇，史诗！"
            dure = (random.random()+1) * 60 * 60
        elif rand >= 0.89 and rand < 0.8999:
            reply = "金色传说！"
            dure = (random.random()+1) * 1440 * 60
        elif rand >= 0.8999 and rand < 0.90:
            reply = "卧槽，一包五金？！"
            dure = 30 * 24 * 60 * 60
        else:
            cq = r'[CQ:image,file=file:///'+str(coin_path)+']'
            reply = "哇哇哇哇！！！💃💃💃爆金币了happy！！！\n"+ cq
            dure = 0
        if dure != 0:
            await bot.set_group_ban(group_id=group, user_id=usrid, duration=dure)
    elif usr_is_admin == "member" and bot_is_admin == "member":
        if rand < 0.4:
            reply = "别戳了，再戳烦了！"
        elif rand >= 0.4 and rand < 0.8:
            reply = "你戳你🐎呢？"
        else:
            cq = r'[CQ:image,file=file:///'+str(coin_path)+']'
            reply = "哇哇哇哇！！！💃💃💃爆金币了happy！！！\n"+ cq
    
    await bot.send_group_msg(group_id=group, message=reply)


