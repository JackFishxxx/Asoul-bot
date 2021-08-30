from nonebot import *
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command

tbd = "树洞\n\
炉石代码匹配\n\
迫害\n\
随机发病\n\
随机溜冰\n\
随机二创图片\n\
A楼高加鹅扣鹅楼层内容"

@on_command("tbd")
async def _(session: CommandSession):
    await session.send(tbd)
