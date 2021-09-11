import time
from hashlib import md5
from nonebot.plugin import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import re

a = '向晚, 晚晚, 幽默钻头, 兄弟, 我兄弟, 晚比, 晚'
b = '贝拉, 拉姐, 拉'
c = '珈乐, 小狼王, 乐'
d = '嘉然, 然然, 粉色小矮子, 粉色小恶魔, 小羽毛球, 粉色小猪猪, 然比, 然'
e = '乃琳, n0, 白色香顶边, 坏女人, 琳'
ab = '师徒组, 师徒, 憨次方'
ac = '萤火虫'
ad = '嘉晚饭'
ae = '果丹皮'
bc = '贝贝珈'
bd = '超级嘉贝'
be = '乃贝, 奶贝'
cd = 'c++, c嘉珈, c珈嘉'
ce = '珈特琳'
de = '母女组'
cao = '阿草, 羊驼, 臭羊驼'
shark = '七海, 海子姐, nanami'

names = [a, b, c, d, e, ab, ac, ad, ae, bc, bd, be, cd, ce, de, cao, shark]


rp = on_keyword(['人品','运势'], rule=to_me(), priority=5)
@rp.handle()
async def return_rp(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).replace('人品','').replace('运势','').replace('的','').replace(',','').replace(' ','').replace('，','')
    if args:
        rpname = args  #先把运势对象复制给usrname
        usrname = args  #用户所输入对象
        for name in names:
            if re.search(args, name):
                rpname = name  # 如果是特定人物则赋值特殊字符串
    else:
        rpname = event.get_user_id() #如果len为1则求用户自身
        usrname = event.get_user_id() 
    usrqq = event.get_user_id()
    
    ret_rp = await get_rp(usrname, usrqq, rpname)
    await rp.finish(ret_rp)
    
async def get_rp(usrname: str, usrqq: str, rpname: str):
    
    t =  time.localtime(time.time())
    rand = t.tm_year + t.tm_yday
    raw = str(rand) + rpname
    raw = str(raw)
    md5_con = md5(raw.encode('utf8')).hexdigest()
    s = [i for i in md5_con if i.isnumeric()]
    rp = str(int("".join(s))%101)
    rely = [{
        "type": "at",
        "data": {
            "qq": usrqq,
            "name": ""
        }
    },
    {
            "type": "text",
            "data": {
                "text": "的运势为："
            }
    },
    {
            "type": "text",
            "data": {
                "text": rp
            }
    }
    ]
    if usrname == rpname:
        rely.insert(1,
            {
            "type": "text",
            "data": {
                "text": '你',
            }
        })
    else:
        rely.insert(1,
            {
            "type": "text",
            "data": {
                "text": usrname,
            }
        })
    return rely