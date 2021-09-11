from nonebot import on_command
import re
import random
import json
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me

obj = open(r'.\src\assist\jjz.json','rb')
data = json.load(obj)
emo = data['emotions']
emoji = emo['emoji']
#xhs = emo['xiaohongshu']
symbols = data['symbols']
auxiliary_words = data['auxiliaryWords']
dividers = data['dividers']
begin = data['beginning']
who = data['who']
someone = data['someone']
todo = data['todosth']
#another = data['another']
end = data['ending']
collect = data['collections']
attr = data['attribute']
fashion = data['fashion']

def ran(ilist):
    random.shuffle(ilist)
    return ilist[0]

jjz = on_command('绝绝子', aliases={'jjz'}, rule=to_me(), priority=5)

@jjz.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message()).split(' ')

    if msg[0] == '':
        await jjz.reject(message="格式不对啦，请加空格和事件")
    else:
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
        tmp = tmp.replace("dosth",str(msg[0]))
        await jjz.finish(message=tmp)