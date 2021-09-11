from bilibili_api import user
import json
import nonebot
from nonebot.plugin import require


obj = open(r'.\global.json','rb')
data = json.load(obj)
qqgroup = data['test_group']
uid = data["slice_uid"] + data["asoul_uid"]

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', hours=12, id="get_slice")
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
    title_obj = open(r'.\src\assist\title.json','w')
    json.dump(title, title_obj)
    pic_obj = open(r'.\src\assist\pic.json','w')
    json.dump(pic, pic_obj)
    url_obj = open(r'.\src\url.json','w')
    json.dump(url, url_obj)
    await bot.send_group_msg(group_id=qqgroup,message = 'slice updated')