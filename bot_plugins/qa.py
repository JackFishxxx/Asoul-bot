from nonebot import *
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
from aiocqhttp import MessageSegment
from bilibili_api import user
import re

@on_command('QA',aliases=('qa','我QA呢','我qa呢'))
async def _(session: CommandSession):
    u = user.User(703007996)
    page = await u.get_articles(0)
    articles = page['articles']
    ar_len = len(articles)
    for i in range(0,ar_len):
        push = articles[i]
        title = push['title']
        matchobj = re.search( r'QA', title, re.M|re.I)
        if matchobj:
            id = push['id']
            url = r'https://www.bilibili.com/read/cv' + str(id)
            summary = push['summary']
            rely=[
                {
                    "type" : "text",
                    "data" : {
                        "text" : title + '\n' + url + '\n' + summary
                    }
                }
            ]
            await session.send(message=rely)
            break
        else:
            pass
