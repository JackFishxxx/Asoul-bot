import json
import os
import random
from warnings import catch_warnings
from nonebot import on_command, on_startswith
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State
import requests
import nonebot
from nonebot.rule import to_me

dice = on_command("r", aliases={"roll", ".r"}, rule=to_me(), priority=5, block=True)

@dice.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):

    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message())  #
    usrid = str(event.get_user_id())

    try:
        (x, y) = msg.split("d")
        x, y = int(x), int(y)
        sum = 0
        for i in range(x):
            sum += random.randint(1, y)
        
        reply = '[CQ:at,qq='+str(usrid)+']'
        reply += str(sum)
        
        await bot.send_group_msg(group_id=group, message=reply)
    except ValueError:
        await bot.send_group_msg(group_id=group, message="格式错误！请输入xdy来表示roll x个y面的骰子点数之和。")

