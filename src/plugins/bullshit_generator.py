import nonebot
from nonebot import on_command
import re
import random
import json
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

obj = open(r'.\src\assist\gpbt.json','rb')
data = json.load(obj)
famous = data['famous']
before = data['before']
after = data['after']
bosh = data['bosh']
xx = ''
repeat = 2

def ran(ilist):
    global repeat
    pool = list(ilist)*repeat
    while True:
        random.shuffle(pool)
        for item in pool:
            yield item

next_bosh = ran(bosh)
next_famous = ran(famous)

def some_famous():
    global next_famous
    xx = next(next_famous)
    xx = xx.replace("a",random.choice(before))
    xx = xx.replace("b",random.choice(after))
    return xx

def another():
    xx = "。"
    xx += "\n"
    xx += "    "
    return xx

bullshit = on_command('狗屁不通', aliases={'bullshit'}, rule=to_me(), priority=5)

@bullshit.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message()).split(' ')

    if msg[0] == '':
        await bullshit.reject(message="格式不对啦，请加空格和主题")
    else:
        xx = msg[0]
        tmp = str()
        while ( len(tmp) < 200 ) :
            k = random.randint(0,100)
            if k < 5:
                tmp += another()
            elif k < 20 :
                tmp += some_famous()
            else:
                tmp += next(next_bosh)
        tmp = tmp.replace("x",xx)
        await bullshit.finish(message=tmp)