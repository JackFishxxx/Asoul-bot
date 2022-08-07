from nonebot import on_command
import os
import random
import json
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

def ran(ilist):
    random.shuffle(ilist)
    return ilist[0]

jjz = on_command('绝绝子', aliases={'jjz'}, rule=to_me(), priority=5, block=True)

@jjz.handle()
async def _(bot: Bot, event: Event):

    msg = str(event.get_message()).split("绝绝子 ")
    group = int(event.get_session_id().split("_")[1])

    if len(msg) == 1:
        reply = "格式错误，应为：绝绝子 话题"
    else:

        assist_path = bot.config.assist_path
        data_path = os.path.join(os.getcwd(), assist_path, 'jjz.json')
        with open(data_path,'rb') as fp:
            data = json.load(fp)

        emo = data['emotions']
        emoji = emo['emoji']
        symbols = data['symbols']
        auxiliary_words = data['auxiliaryWords']
        dividers = data['dividers']
        begin = data['beginning']
        who = data['who']
        someone = data['someone']
        todo = data['todosth']
        end = data['ending']
        collect = data['collections']
        attr = data['attribute']
        fashion = data['fashion']

        tmp = str()
        tmp += ran(begin)
        tmp += ran(emoji) + ran(dividers)
        tmp += ran(fashion) + ran(dividers)
        tmp += ran(todo) + ran(dividers)
        tmp += ran(attr) + ran(symbols)
        tmp += ran(collect) + ran(dividers)
        tmp += ran(fashion) + ran(dividers)
        tmp += ran(auxiliary_words)*3 + ran(dividers)
        tmp += ran(end) + ran(emoji)

        tmp = tmp.replace("who",ran(who))
        tmp = tmp.replace("someone",ran(someone))
        tmp = tmp.replace("dosth",str(msg[1]))

        reply = tmp

    await bot.send_group_msg(group_id=group, message=reply)