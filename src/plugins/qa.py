from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from bilibili_api import user
import re

qa = on_keyword(["qa", "QA"], rule=to_me(), priority=5)

@qa.handle()
async def return_qa(bot: Bot, event: Event, state: dict):

    ret_qa = await get_qa()
    await qa.finish(ret_qa)


async def get_qa():

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
            return rely
        else:
            pass