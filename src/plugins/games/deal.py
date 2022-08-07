import json
import os
from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from nonebot.typing import T_State

buy = on_command('购买', rule=to_me(), priority=5, block=True)

@buy.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).split()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    usrid = str(event.get_user_id())
    if len(args) == 2:
        good = args[0]
        num = args[1]
        state["buyer"] = usrid  # 如果用户发送了参数则直接赋值
        state["good"] = good
        state["num"] = int(num)
    else:
        reply = [{
        "type": "at",
        "data": {
            "qq": usrid,
            "name": ""
            }
        },
        {
        "type": "text",
        "data": {
            "text":"格式错误，格式为购买+空格+物品+空格+数量"
            }
        }
        ]
        await buy.finish(message=reply)

    path = './src/data/users/{}.json'.format(state["buyer"])
    good = state["good"]
    num = state["num"]
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as json_file:
            usr = json.load(json_file)
        usrinfo = usr["usrinfo"]
        money = usrinfo["money"]
        
        all_goods = './src/data/goods/all_goods.json'
        with open(all_goods, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        price = data[good]  #读取物品单价
        if money - price * num < 0: # 如果钱不够
            reply = [{
                "type": "at",
                "data": {
                    "qq": state["buyer"],
                    "name": ""
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "钱不够！"
                }
            }
            ]
            await buy.finish(message=reply)
        else: #如果钱够
            rest_money = money - price * num
            usr['usrinfo']["money"] = rest_money
            if good in usr['goods'].keys():
                usr['goods'][good] = usr['goods'][good] + num
            else:
                usr['goods'][good] = num
            with open(path, 'w', encoding='utf-8') as json_file:
                json.dump(usr, json_file)
            reply = [{
                "type": "at",
                "data": {
                    "qq": state["buyer"],
                    "name": ""
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "购买成功！"
                }
            }
            ]
            await buy.finish(message=reply)
    else:
        reply = [{
                "type": "at",
                "data": {
                    "qq": state["buyer"],
                    "name": ""
                }
            },
            {
                "type": "text",
                "data": {
                    "text": "您还未注册！"
                }
            }
            ]
        await buy.finish(message=reply)