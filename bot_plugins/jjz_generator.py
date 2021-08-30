import nonebot
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import re
import random
import json

bot = nonebot.get_bot()
obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\jjz.json','rb')
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

@on_command('绝绝子')
async def _(session: CommandSession):
    eve = session.event
    msg = eve['message']
    txt = re.sub(r'\u7edd\u7edd\u5b50','',str(msg),count=1)
    txt = txt.strip()
    if txt == '':
        await session.send(message="格式不对啦，请加空格和事件")
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
        tmp = tmp.replace("dosth",str(txt))
        await session.send(message=tmp)