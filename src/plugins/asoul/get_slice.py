from bilibili_api import user
import json
import nonebot
from nonebot.plugin import require
import os

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', hours=12, id="get_slice")
async def main():
    bot = nonebot.get_bot()

    uid_list = bot.config.slice + bot.config.asoul
    test_group = bot.config.test_group

    tid = 0
    pn = 1
    title = []
    url = []
    pic = []
    vlist = []
    for uid in uid_list:
        u = user.User(uid)
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
    
    title_path = os.path.join(os.getcwd(),bot.config.assist_path,'title.json')
    title_obj = open(title_path,'w')
    json.dump(title, title_obj)
    pic_path = os.path.join(os.getcwd(),bot.config.assist_path,'pic.json')
    pic_obj = open(pic_path,'w')
    json.dump(pic, pic_obj)
    url_path = os.path.join(os.getcwd(),bot.config.assist_path,'url.json')
    url_obj = open(url_path,'w')
    json.dump(url, url_obj)
    
    await bot.send_group_msg(group_id=test_group,message = 'slice updated')