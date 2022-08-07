from nonebot import on_command
import random
import os
import json
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

def ran(ilist, repeat):
    pool = list(ilist) * repeat
    while True:
        random.shuffle(pool)
        for item in pool:
            yield item

def some_famous(famous, before, after):
    xx = next(famous)
    xx = xx.replace("a",random.choice(before))
    xx = xx.replace("b",random.choice(after))
    return xx

def another():
    xx = "。"
    xx += "\n"
    xx += "    "
    return xx

bullshit = on_command('狗屁不通', rule=to_me(), priority=5, block=True)

@bullshit.handle()
async def _(bot: Bot, event: Event):
    
    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message()).split(" ")

    if len(msg) == 1:
        
        reply = "格式错误，应为：狗屁不通 主题"

    else:

        assist_path = bot.config.assist_path
        data_path = os.path.join(os.getcwd(), assist_path, 'bullshit.json')
        with open(data_path,'rb') as fp:
            data = json.load(fp)
        
        famous = data['famous']
        before = data['before']
        after = data['after']
        bosh = data['bosh']
        xx = ''
        repeat = 2

        xx = msg[1]
        next_bosh = ran(bosh, repeat)
        next_famous = ran(famous, repeat)
        tmp = str()
        while ( len(tmp) < 200 ) :
            k = random.randint(0,100)
            if k < 5:
                tmp += another()
            elif k < 20 :
                tmp += some_famous(next_famous, before, after)
            else:
                tmp += next(next_bosh)
        reply = tmp.replace("x" ,xx)
    
    await bot.send_group_msg(group_id=group, message=reply)