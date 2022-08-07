from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import json
import os

all_goods = on_command('查询全部物品', aliases={'查询所有物品'}, rule=to_me(), priority=5, block=True)

@all_goods.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())

    path = r'./src/data/goods/all_goods.json'
    with open(path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
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
            "text":"\n{0:{2}<10}\t{1:{2}<5}".format('物品', '价格', chr(12288))
            }
        }
    ]
    for name, price in data.items():
        reply.insert(2,{
            "type": "text",
            "data": {
                "text":"\n{0:{2}<10}\t{1:{2}<5}".format(str(name), str(price), chr(12288))
            }
        })
    await all_goods.finish(message=reply)

good_detail = on_command('查询物品详情', rule=to_me(), priority=5, block=True)

@good_detail.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    usrmsg = str(event.get_message())

    path = r'./src/data/goods/{}.json'.format(usrmsg)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        name = data['name']
        detail = data['detail']
        use = data['use']
        price = data['price']
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
                        "text": "\n名称："+str(name)+"\n描述：\n\t"+str(detail)+"\n用途：\n\t"+str(use)+"\n价格："+str(price)
                    }
            }
            ]

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
                        "text": "该物品不存在！"
                    }
            }
            ]
    await good_detail.finish(message=reply)