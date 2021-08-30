from apscheduler.schedulers.blocking import BlockingScheduler
from bilibili_api import user
import json
import nonebot
qqgroup = 752408143
uid = [393396916,7085311,672346917,672353429,351609538,672328094,672342685,703007996]
@nonebot.scheduler.scheduled_job('interval', hours=12)
async def main():
    bot = nonebot.get_bot()
    tid = 0
    pn = 1
    title = []
    url = []
    pic = []
    vlist = []
    for m in range(0,len(uid)):
        u = user.User(uid[m])
        while True:
            videos = await u.get_videos(tid,pn)
            lists = videos['list']
            vlist = lists['vlist'] + vlist
            page = videos['page']
            ps = page['ps']
            count = page['count']
            if pn*ps > count:
                pn = 1
                break
            else:
                pn = pn + 1
    length = len(vlist)
    i = 0
    while i < length:
        t = vlist[i]['length']
        leng = len(t)
        t = t[0:leng-3]
        t = int(t)
        if t < 30:
            title.append(vlist[i]['title'])
            pic.append(vlist[i]['pic'])
            bvid = vlist[i]['bvid']
            url.append(r'https://www.bilibili.com/video/' + bvid)
            i = i + 1
        else:
            i = i + 1
            pass
    title_obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\title.json','w')
    json.dump(title, title_obj)
    pic_obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\pic.json','w')
    json.dump(pic, pic_obj)
    url_obj = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\url.json','w')
    json.dump(url, url_obj)
    await bot.send_group_msg(group_id=qqgroup,message = 'slice updated')