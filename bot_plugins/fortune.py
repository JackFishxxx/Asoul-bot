# -*- coding: utf-8 -*-
from nonebot import *
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import time
from hashlib import md5
import random

#早期代码，还不明白插件内函数调用规则

def cal(rp):
    rp = str(rp)
    md5_con = md5(rp.encode('utf8')).hexdigest()
    s = [i for i in md5_con if i.isnumeric()]
    s = "".join(s)
    s = int(s)
    rp = s%101
    return rp

@on_command('向晚运势',aliases=('晚晚运势','幽默钻头运势','兄弟运势','我兄弟运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Ava = cal(712 + t)
    txt = ['“顶碗！顶碗！干饭用铲！别人有伞！你有向晚！不开心的时候，就来看我！有兄弟我给你们带来快乐！！”','这里是AvA向晚，懒羊羊不偷懒，钻头不暂缓，喜欢要直接，告白不气喘！']
    length = len(txt)
    i = random.randint(0,length-1)
    await session.send("幽默钻头的今日运势为："+str(Ava)+"\n"+txt[i])

@on_command('贝拉运势',aliases=('拉姐运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Bel = cal(729 + t)
    txt = ['拉姐别打晚晚了要打就打然然吧！','“贝极星们都要多运动注意身体、早点睡觉、多喝热水！这样，我们才能在一起越走越远哦！”']
    length = len(txt)
    i = random.randint(0,length-1)
    await session.send("贝元甲的今日运势为："+str(Bel)+"\n"+txt[i])

@on_command('珈乐运势',aliases=('小狼王运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Cal = cal(1121 + t)
    txt = ['草莓袜子真不是我的','““骑士还爱着你骑士还想着你耶~ 请你别太得意” 回家了太开心了,大家久等了~”']
    length = len(txt)
    i = random.randint(0,length-1)
    await session.send("小狼王的今日运势为："+str(Cal)+"\n"+txt[i])

@on_command('嘉然运势',aliases=('然然运势','粉色小矮子运势','粉色小恶魔运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Dia = cal(314 + t)
    txt = ['嘉心糖屁用没有','“嘉心糖们都一定要好好吃饭捏！”']
    length = len(txt)
    i = random.randint(0,length-1)
    await session.send("圣嘉然的今日运势为："+str(Dia)+"\n"+txt[i])

@on_command('乃琳运势',aliases=('n0运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Eil = cal(808 + t)
    txt = ['乃琳大腿别着凉了','“我永远希望我们能够不疲惫的双向奔赴～”']
    length = len(txt)
    i = random.randint(0,length-1)
    await session.send("香顶边的今日运势为："+str(Eil)+"\n"+txt[i])

@on_command('阿草运势',aliases=('臭羊驼运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Aca = cal(1024 + t)
    await session.send("臭羊驼的今日运势为："+str(Aca)+"\n小伙伴们大家好，在今天的QA开始之前...")

@on_command('七海运势',aliases=('海子姐运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    nanami = cal(773 + t)
    await session.send("大A特A的今日运势为："+str(nanami)+"\nybb")

@on_command('嘉晚饭运势')
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Ava = cal(712 + t)
    Dia = cal(314 + t)
    jwf = cal(Ava + Dia + Ava*Dia)
    await session.send("嘉晚饭的今日运势为："+str(jwf))

@on_command('奶贝运势',aliases=('乃贝运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Bel = cal(729 + t)
    Eil = cal(808 + t)
    nb = cal(Bel + Eil + t)
    await session.send("乃贝的今日运势为："+str(nb))

@on_command('果丹皮运势')
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Ava = cal(712 + t)
    Eil = cal(808 + t)
    gdp = cal(Ava + Eil + t)
    await session.send("果丹皮的今日运势为："+str(gdp))

@on_command('贝贝珈运势')
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Bel = cal(729 + t)
    Cal = cal(1121 + t)
    bbj = cal(Bel + Cal + t)
    await session.send("贝贝珈的今日运势为："+str(bbj))

@on_command('师徒组运势',aliases='憨次方运势')
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Ava = cal(712 + t)
    Bel = cal(729 + t)
    stz = cal(Ava + Bel + t)
    await session.send("师徒组的今日运势为："+str(stz))

@on_command('母女组运势')
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Dia = cal(314 + t)
    Eil = cal(808 + t)
    mnz = cal(Dia + Eil + t)
    await session.send("母女组的今日运势为："+str(mnz))

@on_command('超级嘉贝运势')
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Bel = cal(729 + t)
    Dia = cal(314 + t)
    cjjb = cal(Bel + Dia + t)
    await session.send("超级嘉贝的今日运势为："+str(cjjb))

@on_command('珈特琳运势')
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Cal = cal(1121 + t)
    Eil = cal(808 + t)
    jtl = cal(Cal + Eil + t)
    await session.send("珈特琳的今日运势为："+str(jtl))

@on_command('萤火虫运势',aliases=('头号晚珈运势'))
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Cal = cal(1121 + t)
    Ava = cal(712 + t)
    yhc = cal(Cal + Ava + t)
    await session.send("头号晚珈的今日运势为："+str(yhc))

@on_command('c++运势')
async def _(session: CommandSession):
    t = time.localtime()
    tm = int(t.tm_mday)
    ty = int(t.tm_yday)
    t = tm*ty
    Cal = cal(1121 + t)
    Dia = cal(314 + t)
    cpp = cal(Cal + Dia +t)
    await session.send("c++的今日运势为："+str(cpp))