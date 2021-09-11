import json
from os import path
import nonebot
from bilibili_api import live
from nonebot import require

old_status = [-1,-1,-1,-1,-1,-1]

obj = open(r'.\global.json','rb')
data = json.load(obj)

qqgroup = data['all']
qq_noshark = data['no_shark']
qq_len = len(qqgroup)
qq_noshark_len = len(qq_noshark)

uid_asoul = data['live_uid']
uid_all = data['live_uid'] + data['shark_live']
uid_len = len(uid_all)

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', minutes=3, id="get_live")
async def main():
    bot = nonebot.get_bot()
    for i in range(0,uid_len):      
        global old_status
        room = live.LiveRoom(uid_all[i])
        info = await room.get_room_info()
        room_info = info['room_info']
        title = room_info['title']
        cover = room_info['cover']
        print(cover)
        live_status = room_info['live_status']
        #live_start_time = room_info['live_start_time']
        url = r"https://live.bilibili.com/" + str(uid_all[i])
        if live_status == old_status[i]:
            pass
        elif live_status == 1:
            rely = [
                {
                "type": "text",
                "data": {
                    "text": title + '\n' + url
                }
            },
                {
                "type": "image",
                "data": {
                    "file" : cover
                }
            }]
            if i == 5:
                for j in range(0,qq_len):
                    old_status[i] = live_status
                    await bot.send_group_msg(group_id=qqgroup[j],message=rely)
            else:
                for k in range(0,qq_len):
                    old_status[i] = live_status
                    await bot.send_group_msg(group_id=qqgroup[k],message=rely)
                for m in range(0,qq_noshark_len):
                    old_status[i] = live_status
                    await bot.send_group_msg(group_id=qq_noshark[m],message=rely)
        else:
            old_status[i] = live_status
