import json
import re
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
from nonebot.typing import T_State
import requests

music = on_command("点歌", rule=to_me(), priority=5, block=True)

@music.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):

    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message())  #

    app_url = bot.config.music

    typ = "1"
    info = re.findall(r'第[1-9][0-9]*首', msg)
    if info == []:
        info = ["第1首"]
    info = info[0]
    msg = msg.replace("点歌 ", "").replace(info, '')
    num = info.replace("第", '').replace('首', '')
    #api = "http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20".format(msg)
    api = app_url + r"/cloudsearch?keywords={}&type={}&limit=50".format(msg, typ)
    response = requests.get(api)
    response = response.text
    html = json.loads(response)
    id = html['result']['songs'][int(num)-1]['id']

    
    cq = "[CQ:music,type=163,id={}]".format(id)
        
    await bot.send_group_msg(group_id=group, message=cq)

program = on_command("声音", rule=to_me(), priority=5, block=True)

@program.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):

    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message())  #

    app_url = bot.config.music
    
    typ = "2000"
    info = re.findall(r'第[1-9][0-9]*首', msg)
    if info == []:
        info = ["第1首"]
    info = info[0]
    msg = msg.replace("声音 ", "").replace(info, '')
    num = info.replace("第", '').replace('首', '')
    #api = "http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20".format(msg)
    api = app_url + r"/search?keywords={}&type={}&limit=50".format(msg, typ)
    response = requests.get(api)
    response = response.text
    html = json.loads(response)
    id = html['data']['resources'][int(num)-1]['baseInfo']['mainSong']['id']
    cq = "[CQ:music,type=163,id={}]".format(id)
        
    await bot.send_group_msg(group_id=group, message=cq)

singer = on_command("歌手", rule=to_me(), priority=5, block=True)

@singer.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):

    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message())  #

    app_url = bot.config.music
    
    typ = "100"
    info = re.findall(r'第[1-9][0-9]*首', msg)
    if info == []:
        info = ["第1首"]
    info = info[0]
    msg = msg.replace("歌手 ", "").replace(info, '')
    num = info.replace("第", '').replace('首', '')
    #api = "http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20".format(msg)
    api = app_url + r"/cloudsearch?keywords={}&type={}".format(msg, typ)
    response = requests.get(api)
    response = response.text
    html = json.loads(response)
    aid = html['result']['artists'][0]['id']

    songapi = app_url + r"/artists?id={}".format(aid)
    response = requests.get(songapi)
    response = response.text
    html = json.loads(response)
    sid = html['hotSongs'][int(num)-1]['id']
    cq = "[CQ:music,type=163,id={}]".format(sid)
        
    await bot.send_group_msg(group_id=group, message=cq)

album = on_command("专辑", rule=to_me(), priority=5, block=True)

@album.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):

    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message())  #

    app_url = bot.config.music
    
    typ = "10"
    info = re.findall(r'第[1-9][0-9]*首', msg)
    if info == []:
        info = ["第1首"]
    info = info[0]
    msg = msg.replace("专辑 ", "").replace(info, '')
    num = info.replace("第", '').replace('首', '')
    #api = "http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20".format(msg)
    api = app_url + r"/cloudsearch?keywords={}&type={}".format(msg, typ)
    response = requests.get(api)
    response = response.text
    html = json.loads(response)
    aid = html['result']['albums'][0]['id']

    songapi = app_url + r"/album?id={}".format(aid)
    response = requests.get(songapi)
    response = response.text
    html = json.loads(response)
    sid = html['songs'][int(num)-1]['id']
    cq = "[CQ:music,type=163,id={}]".format(sid)
        
    await bot.send_group_msg(group_id=group, message=cq)
    
    
    
    