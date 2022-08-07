import random
import json
import os
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event

startProb = 0.3
endProb = 0.3

def getRandomThing(arr, name):
    min = 0
    max = len(arr) - 1
    
    rand = random.randint(min, max)
    result = arr[rand].replace("XXX", str(name)).replace("NAME", str(name))
    return result


def getRandomItem(arr):
    rand = random.randint(0, len(arr) - 1)
    return arr[rand]


def generateSentence(name, data):
    sentence = ""

    sentenceStart = data["sentenceStart"]
    sentenceEnd = data["sentenceEnd"]
    caihongpi = data["caihongpi"]
    qinghua = data["qinghua"]

    rand = random.random()
    if(rand > startProb):
        sentence += getRandomThing(sentenceStart, name)
    
    mainPart = getRandomItem([caihongpi, qinghua])
    sentence += getRandomThing(mainPart, name)
    rand = random.random()
    if(rand > endProb):
        sentence += getRandomThing(sentenceEnd, name)

    return addDot(sentence)
    
def addDot(str):
    if(str[len(str) - 1] != "。"):
        str += "。"
    
    return str

def generatePart(name, data):
    part = ""
    rand = random.random()
    partStart = data["partStart"]
    if(rand > startProb):
        part += getRandomThing(partStart, name)
    
    sentenceCount = random.randint(1, 3)
    for i in range(0, sentenceCount):
        part += generateSentence(name, data)

    partEnd = data["partEnd"]
    rand = random.random()
    if(rand > endProb):
        part += getRandomThing(partEnd, name)
    
    return part

def generateContent(name, data):
    content = name + "！"
    rand = random.randint(1, 3)
    for i in range(0, rand):
        content += generatePart(name, data)
    
    qinghua = data["qinghua"]
    content += addDot(getRandomThing(qinghua, name))
    return content

chp = on_command("彩虹屁", rule=to_me(), priority=5, block=True)

@chp.handle()
async def return_chp(bot: Bot, event: Event):

    usrmsg = str(event.get_message()).split("彩虹屁 ")
    group = int(event.get_session_id().split("_")[1])

    if len(usrmsg) == 1:
        reply = "格式错误，应为：彩虹屁 话题"
    else:

        assist_path = bot.config.assist_path
        data_path = os.path.join(os.getcwd(), assist_path, 'chp.json')
        with open(data_path,'rb') as fp:
            data = json.load(fp)

        usrmsg = usrmsg[1]
        reply = generateContent(usrmsg, data)

    await bot.send_group_msg(group_id=group, message=reply)

