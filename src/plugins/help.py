# -*- coding: utf-8 -*-
from nonebot import *
from nonebot.plugin import on_keyword
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

help = on_keyword(['帮助', 'help', '功能'], rule=to_me())

@help.handle()
async def handle_help(bot: Bot, event: Event, state: T_State):
    ret_help = await get_help(help)
    await help.finish(ret_help)

async def get_help(help: str):
    return f"使用方法：@bot然后输入指令\n\
已实现功能：\n\
-输入关键词 “帮助/help/功能” 获取帮助菜单\n\
-输入指令   “冷笑话/笑话” 获取随机冷笑话\n\
-输入关键词 “运势+空格/逗号+版本强势CP名/人物” 获取该人物/cp今日运势\n\
-输入关键词 “日程表” 获取本周日程表\n\
-输入指令   “实时粉丝数/粉丝数” 获取AS五人+阿草+海子姐实时粉丝数\n\
-输入指令   “人品/运势” 获取你今日的运势\n\
-输入指令   “remake/重开” 获取重开结果\n\
-输入关键词 “QA/qa” 获取本周QA\n\
-输入关键词 “午饭/晚饭/夜宵/吃”等 获取你到底吃啥（带学生不吃早饭和下午茶！）\n\
-输入指令   “小作文” 获取随机小作文\n\
-输入指令   “狗屁不通”+空格+主题 生成一段狗屁不通的文章\n\
-输入指令   “概率”+空格+事件 获取某事发生的概率\n\
-输入指令   “绝绝子”+空格+事件 生成绝绝子小短文\n\
-输入指令   “匹配”+空格+匹配对象 测试你和ta的匹配程度吧\n\
-输入指令   “表情包” 获取随机表情包（感谢洛骑塔的收集）\n\
-输入指令   “切片” 获取随机切片（感谢贾布加布和珈然今晚吃奶贝两位切片man）\n\
-输入指令   “识图”+空格+图片 返回百度识图结果（有待完善）\n\
推送功能：\n\
    -开播提醒\n\
    -动态发布提醒\n\
    -日程表发布提醒\n\
    -抖音小视频发布提醒\n\
如果bot没有反应看看是不是复制了别人的命令或者格式不对？需要自己手动艾特bot哦"