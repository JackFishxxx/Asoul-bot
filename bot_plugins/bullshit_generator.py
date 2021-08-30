import nonebot
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import re
import random
import json

bot = nonebot.get_bot()
obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\gpbt.json','rb')
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
    xx = xx.replace(  "a",random.choice(before) )
    xx = xx.replace(  "b",random.choice(after) )
    return xx

def another():
    xx = ". "
    xx += "\n"
    xx += "    "
    return xx

@on_command('狗屁不通')
async def _(session: CommandSession):
    eve = session.event
    msg = eve['message']
    txt = re.sub(r'\u72d7\u5c41\u4e0d\u901a','',str(msg),count=1)
    txt = txt.strip()
    if txt == '':
        await session.send(message="格式不对啦，请加空格和主题")
    else:
        xx = txt
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
        await session.send(message=tmp)