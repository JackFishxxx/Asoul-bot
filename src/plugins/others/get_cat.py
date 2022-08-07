import json
import nonebot
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
import requests

cat = on_command("猫猫", rule=to_me(), priority=5, block=True)

@cat.handle()
async def return_cat(bot: Bot, event: Event):

    group = int(event.get_session_id().split("_")[1])

    url = 'https://aws.random.cat/meow'
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Mobile Safari/537.36',
    }
    html = requests.get(url, headers=headers)
    html = html.text
    data = json.loads(html)
    link = data['file']

    cq = r'[CQ:image,file='+str(link)+']'

    await bot.send_group_msg(group_id=group, message=cq)
    