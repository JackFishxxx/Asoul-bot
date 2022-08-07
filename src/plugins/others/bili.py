import json
from nonebot import on_command
from nonebot.adapters import Bot, Event
from nonebot.rule import to_me
import requests

bili = on_command("b站", aliases={"bili", "B站"}, rule=to_me(), priority=5, block=True)

@bili.handle()
async def handle_first_receive(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])
    msg = str(event.get_message())

    api = r"http://api.bilibili.com/x/web-interface/search/all/v2?keyword={}".format(msg)
    response = requests.get(api)
    response = response.text
    html = json.loads(response)
    id = html['data']['result'][10]['data'][0]['bvid']

    api = "https://api.bilibili.com/x/web-interface/view?bvid="+id
    response = requests.get(api)
    response = response.text
    html = json.loads(response)
    title = html['data']['title']
    pic = html['data']['pic']
    up = html['data']['owner']['name']
    url = "https://www.bilibili.com/"+id
    cq = r'[CQ:image,file='+str(pic)+']'
    msg = "视频标题：{}\nUP主：{}\n{}\n{}".format(title, up, url, cq)
        
    await bot.send_group_msg(group_id=group, message=msg)

