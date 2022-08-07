# -*- coding: utf-8 -*-
from nonebot.plugin import on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event

help = on_command('帮助', aliases={'help', '功能'}, rule=to_me(), priority=2, block=True)

@help.handle()
async def handle_help(bot: Bot, event: Event, state: T_State):
    ret_help = await get_help(help)
    await help.finish(ret_help)

async def get_help(help: str):
    return f"使用方法：@bot然后输入指令\n\
-输入指令 “常用/常用功能” 获取常用功能详细介绍\n\
-输入指令 “注意/注意事项” 获取注意事项\n\
-输入指令 “游戏” 获取（做到一半的）游戏帮助\n\
-请各位善待bot，欢迎提出意见和建议，除了常用功能外，还请阅读注意事项。\n\
-上新内容：\n\
-现在，指令“匹配”支持“匹配 A B”的格式，将计算A和B的匹配程度。\n\
-现在，项目大幅度重构，按照OneBot V11标准修改，解耦了公共参数便于管理。\n\
-现在，bot支持黑名单功能，在黑名单内的用户将不会触发bot。\n\
-现在，bot支持戳一戳功能，如果bot有管理员权限将会随机禁言。\n\
-现在，bot可以选择直播、动态等信息推送的群和关注的用户了\n\
-输入指令 “说/转语音 内容” 进行文字转语音，上限30个字符\n\
-输入指令 “B站/bili/B站 搜索内容” 进行视频搜索推送\n\
"

usual = on_command('常用', aliases={'常用功能'}, rule=to_me(), priority=2, block=True)

@usual.handle()
async def handle_help(bot: Bot, event: Event, state: T_State):
    ret_usual = await get_usual(usual)
    await usual.finish(ret_usual)

async def get_usual(usual: str):
    return f"使用方法：@bot然后输入指令\n\
常用功能：\n\
-输入关键词 “帮助/help/功能” 获取帮助菜单\n\
-现在，无需@bot，只需输入任意的BV号、B站视频链接、B站直播间链接将会返回标题、UP主和封面。\n\
-输入指令 “emoji表情+emoji表情” 获取emojimix表情\n\
-输入指令 “点歌/声音/专辑/歌手 搜索内容 第x首” 获取点歌内容，如果不加第x首则默认第1首\n\
-输入指令 “疯狂星期四” 获取疯狂星期四小作文\n\
-输入指令 “roll/.r/r xdy” 进行一次掷骰，返回x个y面的骰子点数之和\n\
-输入指令 “色图/涩图” 获取随机色图\n\
-输入指令 “猫猫” 获取随机猫猫\n\
-输入指令 “彩虹屁+主题” 获取彩虹屁小作文\n\
-输入指令   “冷笑话/笑话” 获取随机冷笑话\n\
-输入关键词 “运势+空格/逗号+版本强势CP名/人物” 获取该人物CP今日运势\n\
-输入关键词 “日程表” 获取本周日程表\n\
-输入指令   “实时粉丝数/粉丝数” 获取AS五人+阿草实时粉丝数\n\
-输入指令   “人品/运势” 获取你今日的运势\n\
-输入指令   “remake/重开” 获取重开结果\n\
-输入关键词 “QA/qa” 获取本周QA\n\
-输入关键词 “午饭/晚饭/夜宵/吃”等 获取你到底吃啥（带学生不吃早饭和下午茶！）\n\
-输入指令   “小作文” 获取随机小作文\n\
-输入指令   “狗屁不通”+空格+主题 生成一段狗屁不通的文章\n\
-输入指令   “概率”+空格+事件 获取某事发生的概率\n\
-输入指令   “绝绝子”+空格+事件 生成绝绝子小短文\n\
-输入指令   “匹配”+空格+匹配对象 测试你和ta的匹配程度吧\n\
-输入指令   “表情包” 获取随机表情包（感谢表情包man）\n\
-输入指令   “切片” 获取随机切片（感谢切片man）\n\
推送功能可选开启（请联系管理员）：\n\
    -开播提醒\n\
    -动态发布提醒\n\
    -日程表发布提醒\n\
    -抖音小视频发布提醒\
"

notice = on_command('注意', aliases={'注意事项'}, rule=to_me(), priority=2, block=True)

@notice.handle()
async def handle_notice(bot: Bot, event: Event, state: T_State):
    ret_notice = await get_notice(notice)
    await notice.finish(ret_notice)

async def get_notice(notice: str):
    return f"注意事项：\n\
-使用bot请遵守我国的法律法规！\n\
-bot需要at，如果bot没反应请看下是否蓝了，不要直接复制指令\n\
-本bot已开源，项目地址：https://github.com/JackFishxxx/Asoul-bot \n\
-bot藏有2.5个彩蛋，其中1.5个有提示\n\
-为什么输入彩蛋没有彩蛋：就这还能叫彩蛋？\n\
-游戏没写完，没更新是因为我懒\n\
-为什么不更新：你说呢？\n\
-关于概率功能需要说明的是，如果事件包含有“我”字，则概率会针对个体进行绑定，如果包含有“你”字，则会和bot绑定，如果都没有则是全局概率，任何人输入都一致\n\
-运势会每日0点更新，和日期以及对象（若只是运势二字则求的是用户自身）绑定，范围在0-100\n\
-如果命令蓝了，bot还没反应，那可能是bot睡觉了。bot也是人，请给bot一点休息时间！\n\
-觉得bot不好你就去建设它\n\
-我真的怀疑有些人闲的程度啊\
"

game = on_command('游戏', rule=to_me(), priority=2, block=True)

@game.handle()
async def handle_game(bot: Bot, event: Event, state: T_State):
    ret_game = await get_game(game)
    await game.finish(ret_game)

async def get_game(game: str):
    return f"游戏篇：@bot然后输入指令\n\
-输入指令 “注册” 注册一个新账号 账号与QQ号绑定，一人只能有一个 \n\
-输入指令 “显示/展示所有/全部称号” 显示你当前拥有的所有称号\n\
-输入指令 “显示/展示称号” 展示你所选择的称号，只会展示一个\n\
-输入指令 “修改显示/展示称号+空格+对应称号” 修改想要展示的称号，只能从拥有的称号中修改\n\
-输入指令 “查询所有/全部物品” 查询当前商店内的所有物品和单价\n\
-输入指令 “查询物品详情” 查询对应物品的详细信息，包括物品描述、物品用途、单价等信息\n\
-输入指令 “购买+空格+物品+空格+数字” 购买对应数量的物品，请输入数字\n\
-输入指令 “用户面板/个人信息” 查询你当前的个人信息\n\
-输入指令 “更新” 进行每日商店信息更新（需要管理员权限）\
"
