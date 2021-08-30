import nonebot
from hashlib import md5
from nonebot.command import CommandSession
from nonebot.command.argfilter import extractors, validators
from nonebot.experimental.plugin import on_command
import hashlib

bot = nonebot.get_bot()

@on_command('匹配')
async def _(session: CommandSession):
    eve = session.event
    grp_id = eve['group_id']
    sender = eve['sender']
    usr_id = sender['user_id']
    kind = session.get(
    'kind', prompt='你要测试和谁的匹配程度呢？',
    arg_filters=[
        extractors.extract_text,  # 取纯文本部分
        str.strip,  # 去掉两边空白字符
        # 正则匹配输入格式
        validators.match_regex(r'.+', '格式不对啦，请重新输入')
        ]
    )
    md5_con = md5(kind.encode('utf8')).hexdigest()
    s = [i for i in md5_con if i.isnumeric()]
    s = "".join(s)
    sha_con = hashlib.sha1(kind.encode('utf8')).hexdigest()
    t = [j for j in sha_con if j.isnumeric()]
    t = "".join(t)
    result = int(s) + int(t)
    rp = (result + usr_id)%101
    string = "嗨呀，你和" + str(kind) + "的相配程度竟然是" + str(rp) + '%呀！'
    await bot.send_group_msg(group_id=grp_id,message=string)
