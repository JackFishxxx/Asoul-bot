from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from bilibili_api import user
import re

uid = 703007996

qa = on_command(cmd="qa", aliases={"QA"}, rule=to_me(), priority=5, block=True)

@qa.handle()
async def _(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])

    u = user.User(uid)
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
            reply=[
                {
                    "type" : "text",
                    "data" : {
                        "text" : title + '\n' + url + '\n' + summary
                    }
                }
            ]
            await bot.send_group_msg(group_id=group, message=reply)
            break
        else:
            pass