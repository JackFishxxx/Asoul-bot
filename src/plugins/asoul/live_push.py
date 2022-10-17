﻿import json
import os
import nonebot
import time
from bilibili_api import live
from nonebot.plugin import require

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', minutes=5, id="live_push")
async def main():

    bot = nonebot.get_bot()
    live_list = bot.config.live
    push_groups = bot.config.push_groups

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'asoul.json')
    with open(data_path,'rb') as fp:
        asoul = json.load(fp)
    
    for live_uid in live_list:
        
        room = live.LiveRoom(live_uid)
        info = await room.get_room_info()
        title = info['room_info']['title']
        cover = info['room_info']['cover']
        uid = info['room_info']['uid']
        live_status = info['room_info']['live_status']
        uname = info['anchor_info']['base_info']['uname']
        pushed = asoul[str(uid)]["live"]["pushed"]

        # on streaming but not pushed
        if live_status == 1 and pushed == 0:

            # push
            if live_status == 1:
                status = '直播中'
            else:
                status = '未开播'
            url = r"https://live.bilibili.com/" + str(live_uid)
            cq = r'[CQ:image,file='+str(cover)+']'
            msg = "直播标题：{}\nUP主：{}\n直播状态：{}\n{}\n{}".format(title, uname, status, url, cq)
            
            # update
            asoul[str(uid)]["live"]["pushed"] = 1
            asoul[str(uid)]["live"]["status"] = 1

            for push_group in push_groups:
                try:
                    await bot.send_group_msg(group_id=push_group,message=msg)
                except Exception as e:
                    print("Can not push live!")
        
        # on streaming and pushed
        elif live_status == 1 and pushed == 1:
            # update
            asoul[str(uid)]["live"]["pushed"] = 1
            asoul[str(uid)]["live"]["status"] = 1

        # not streaming
        else:
            # update
            asoul[str(uid)]["live"]["pushed"] = 0
            asoul[str(uid)]["live"]["status"] = 0

    with open(data_path, 'w') as fp:
        json.dump(asoul, fp)
        
