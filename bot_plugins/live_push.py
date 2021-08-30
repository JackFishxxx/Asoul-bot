from os import path
import nonebot
from bilibili_api import live
from aiocqhttp import MessageSegment

old_status = [-1,-1,-1,-1,-1,-1]
uid = [22625025,22632424,22634198,22637261,22625027,21452505]
uid_len = len(uid)
qqgroup = []
qq_noshark = []
qq_len = len(qqgroup)
qq_noshark_len = len(qq_noshark)
bot = nonebot.get_bot()

@nonebot.scheduler.scheduled_job('interval', minutes=3)
async def main():
    for i in range(0,uid_len):      
        global old_status
        room = live.LiveRoom(uid[i])
        info = await room.get_room_info()
        room_info = info['room_info']
        title = room_info['title']
        cover = room_info['cover']
        live_status = room_info['live_status']
        #live_start_time = room_info['live_start_time']
        url = r"https://live.bilibili.com/" + str(uid[i])
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
