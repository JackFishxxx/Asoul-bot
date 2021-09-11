import json
import random
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

img = on_command('表情包', rule=to_me(), priority=5)

@img.handle()
async def _(bot: Bot, event: Event):
    img_obj = open(r'.\src\assist\img.json', 'r')
    img_list = json.load(img_obj)
    length = len(img_list)
    i = random.randint(0,length-1)
    rely = {
        "type" : "image",
        "data" : {
            "file" : r'http://' + img_list[i]
        }
    }
    await img.finish(message=rely)