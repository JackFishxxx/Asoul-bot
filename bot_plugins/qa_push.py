from bilibili_api import user
import re
import nonebot
import time

qqgroup = []
qq_len = len(qqgroup)
uid = 703007996
glo_id = 0
@nonebot.scheduler.scheduled_job('interval', minutes=3)
async def main():
    t = time.localtime()
    tw = t.tm_wday
    bot = nonebot.get_bot()
    if tw == 1:
        u = user.User(uid)
        page = await u.get_articles(0)
        articles = page['articles']
        ar_len = len(articles)
        for i in range(0,ar_len):
            global glo_id
            push = articles[i]
            timestamp = push['publish_time']
            ts = time.time()
            ts = int(ts)
            dif = (ts - timestamp)/600
            title = push['title']
            id = push['id']
            if id == glo_id:
                pass
            elif dif > 1:
                pass
            else:
                matchobj = re.search( r'QA', title, re.M|re.I)
                if matchobj:
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
                    for j in range(0,qq_len):
                        await bot.send_group_msg(group_id=qqgroup[j],message=rely)
                    glo_id = id
                break
    else:
        pass