import json
from bilibili_api import user
import re
import nonebot
import time
from nonebot import require

obj = open(r'.\global.json','rb')
data = json.load(obj)
qqgroup = data['all']
qq_len = len(qqgroup)
uid = 703007996
glo_time = 0

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', minutes=10, id="get_schedule")
async def main():
    t = time.localtime()
    tw = t.tm_wday
    bot = nonebot.get_bot()
    if tw == 1:
        u = user.User(uid)
        page = await u.get_dynamics(0)
        nxt = page['next_offset']
        page2 = await u.get_dynamics(nxt)
        dynamic1 = page['cards']
        dynamic2 = page2['cards']
        dynamic = dynamic1 + dynamic2
        dy_len = len(dynamic)
        for i in range(0,dy_len):
            global glo_time
            dy = dynamic[i]
            desc = dy['desc']
            type = desc['type']
            ts = time.time()
            ts = int(ts)
            timestamp = desc['timestamp']
            dif = dif = (ts - timestamp)/600
            if type != 2:
                pass
            elif dif > 1:
                pass
            elif timestamp == glo_time:
                pass
            else:
                card = dy['card']
                item = card['item']
                des = item['description']
                des = des.encode('utf-8')
                sche = '日程表'
                sche = sche.encode('utf-8')
                matchobj = re.search(sche, des, re.M|re.I)
                if matchobj:
                    pic = item['pictures']
                    url = pic[0]['img_src']
                    rely = [
                        {
                            "type" : "text",
                            "data" : {
                                "text" : "本周日程表：\n"
                            }
                        },
                        {
                            "type": "image",
                            "data": {
                            "file" : url
                            }
                        }
                    ]
                    for j in range(0,qq_len):
                        await bot.send_group_msg(group_id=qqgroup[j],message=rely)
                    glo_time = timestamp
                break
    else:
        pass