from bilibili_api import user
import re
import nonebot
import time
from nonebot import require

uid = 703007996
glo_id = 0

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', minutes=10, id="get_qa")
async def main():

    t = time.localtime()
    tw = t.tm_wday
    bot = nonebot.get_bot()
    
    push_groups = bot.config.push_groups
    
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
                    reply=[
                        {
                            "type" : "text",
                            "data" : {
                                "text" : title + '\n' + url + '\n' + summary
                            }
                        }
                    ]
                    for push_group in push_groups:
                        await bot.send_group_msg(group_id=push_group,message=reply)
                    glo_id = id
                break
    else:
        pass