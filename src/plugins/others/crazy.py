import random
import json
import os
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

crazy = on_command(cmd='疯狂星期四', priority=5, rule=to_me(), block=True)

@crazy.handle()
async def _(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'crazy.json')
    with open(data_path,'rb') as fp:
        data = json.load(fp)

    rand = random.random()
    if rand > 0.3:
        kfc = random.choice(data["text"])
        reply = kfc
    else:
        rand = random.randint(1, len(data["image"]))
        kfc = data["image"][str(rand)]
        reply = "{}[CQ:image,file=base64://{}]".format(kfc[0], kfc[1])

    await bot.send_group_msg(group_id=group, message=reply)