from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import json
import os

update = on_command('更新', rule=to_me(), priority=5, block=True)

@update.handle()
async def _(bot: Bot, event: Event):

    usrid = str(event.get_user_id())
    obj = open(r'.\global.json','rb')
    glob = json.load(obj)
    superuser = glob['superuser'][0]
    if usrid != superuser:
        await update.finish(message="您没有权限！")
    else:
        goods = os.listdir(r'./src/data/goods')
        all_goods = {}
        for good in goods:
            path = r'./src/data/goods/{}'.format(good)
            with open(path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            name = data['name']
            price = data['price']
            all_goods[name] = price
        goods_path = r'./src/data/goods/all_goods.json'
        with open(goods_path, 'w', encoding='utf-8') as json_file:
            json.dump(all_goods, json_file)

    await update.finish(message='数据更新成功！')