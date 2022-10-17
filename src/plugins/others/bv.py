import json
from nonebot import on_startswith
from nonebot.adapters import Bot, Event
import requests
import nonebot
from bilibili_api import live, sync, get_real_url

bv = on_startswith(msg=("https://www.bilibili.com/", "BV", "www.bilibili.com", "https://b23.tv/", "b23.tv", "https://m.bilibili.com", "m.bilibili.com", "av"), priority=5, block=True)

@bv.handle()
async def handle_first_receive(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message())

    # if it is shortlink
    if msg.startswith("https://b23.tv/") or msg.startswith("b23.tv"):
        #url = sync(get_real_url(msg))
        url = await get_real_url(msg)
        #print(dir(url),url.path)
        vid = 'BV'+url.path.split('/')[2].lstrip('BV')
        url = "https://api.bilibili.com/x/web-interface/view?bvid="+vid
    elif msg.startswith("av"):
        vid = msg.split("av")[-1]
        url = "https://api.bilibili.com/x/web-interface/view?aid="+vid
        vid = "av"+vid
    else:
        #print(msg, msg.split('?')[0],msg.split('?')[0].split('BV',1)[1])
        vid = 'BV'+msg.split('?')[0].split('BV',1)[1].rstrip('/')
        url = "https://api.bilibili.com/x/web-interface/view?bvid="+vid
    
    response = requests.get(url)
    response = response.text
    html = json.loads(response)
    title = html['data']['title']
    pic = html['data']['pic']
    up = html['data']['owner']['name']
    url = "www.bilibili.com/"+vid
    cq = r'[CQ:image,file='+str(pic)+']'

    try:
        msg = "视频标题：{}\nUP主：{}\n{}\n{}".format(title, up, url, cq)
    
        await bot.send_group_msg(group_id=group, message=msg)
    except nonebot.adapters.onebot.exception.ActionFailed:

        msg = "视频内容疑似被风控，暂时无法返回信息。"
        #msg = "视频标题：{}\nUP主：{}\n{}\n{}".format(title, up, url, cq)
    
        await bot.send_group_msg(group_id=group, message=msg)
     

blive = on_startswith(msg=("https://live.bilibili.com/", "live.bilibili.com"), priority=5, block=True)

@blive.handle()
async def handle_first_receive(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message())  #
    rid = msg.split('?')[0].split('/')[-1]
  
    room = live.LiveRoom(rid)
    info = await room.get_room_info()
    title = info['room_info']['title']
    cover = info['room_info']['cover']
    live_status = info['room_info']['live_status']
    up = info['anchor_info']['base_info']['uname']
    if live_status == 1:
        status = '直播中'
    else:
        status = '未开播'
    url = r"https://live.bilibili.com/" + str(rid)
    cq = r'[CQ:image,file='+str(cover)+']'
    msg = "直播标题：{}\nUP主：{}\n直播状态：{}\n{}\n{}".format(title, up, status, url, cq)
    
    await bot.send_group_msg(group_id=group, message=msg)

    