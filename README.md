# Asoul-bot
一个基于nonebot2和go-cqhttp的Asoul-bot开源项目，包含了一系列的小功能，可以轻量化地部署在本地从而实现一个有关Asoul的群聊bot。

## 更新内容

1. 现在，项目大幅度重构，按照OneBot V11标准修改，解耦了公共参数便于管理，并重构了帮助菜单。
2. 现在，指令“匹配”支持“匹配 A B”的格式，将计算A和B的匹配程度。
3. 现在，bot支持黑名单功能，在黑名单内的用户将不会触发bot。
4. 现在，bot支持戳一戳功能，如果bot有管理员权限将会随机禁言。
5. 现在，bot可以选择直播、动态等信息推送的群和关注的用户了
6. 输入指令 “说/转语音 内容” 进行文字转语音，上限30个字符
7. 输入指令 “B站/bili/B站 搜索内容” 进行视频搜索推送
8. 现在，无需@bot，只需输入任意的BV号、B站视频链接、B站直播间链接将会返回标题、UP主和封面。
9. 输入指令 “emoji表情+emoji表情” 获取emojimix表情
10. 输入指令 “点歌/声音/专辑/歌手 搜索内容 第x首” 获取点歌内容，如果不加第x首则默认第1首
11. 输入指令 “疯狂星期四” 获取疯狂星期四小作文
12. 输入指令 “roll/.r/r xdy” 进行一次掷骰，返回x个y面的骰子点数之和
13. 输入指令 “色图/涩图” 获取随机色图
14. 输入指令 “猫猫” 获取随机猫猫
15. 输入指令 “彩虹屁+主题” 获取彩虹屁小作文

## 配置运行

1. 首先，下载go-cqhttp客户端。它主要起到了接收消息并传达给Asoul-bot的作用，具体使用详情可以参考以下项目：[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，点击右侧releases进行下载；
2. 按照quick_start的说明文档进行go-cqhttp内 `config.yaml` 文件的配置。[quick_start](https://docs.go-cqhttp.org/guide/quick_start.html)。按照说明配置完成后，登录想要成为bot的账号，并且调试即可；
3. 然后，配置bot信息。先下载nonebot2，请使用[最新版本](https://v2.nonebot.dev/docs/start/installation)；
4. 按照说明编辑 `config.yml` 文件。输入账号密码，以及反向WS设置的universal地址，并且监控地址和端口应与 `.env` 文件中的`HOST`与`PORT`项匹配；
5. 配置bot的 `.env`或 `.env.prod`文件，其中包含了使用的一些全局变量，具体参数信息详见下一节参数配置；
6. (可选) 配置[网易云音乐API](https://github.com/Binaryify/NeteaseCloudMusicApi)，再参考以下[教程](https://blog.csdn.net/SoSalty/article/details/124516171)部署Vercel应用，得到一个应用接口网址如`https://xxx.vercel.app`后，输入配置文件`.env`内的music一项。如不配置则无法使用点歌功能；
7. 使用指令 `pip install -r requirements.txt` 安装必要库；
6. 最后，启动bot。你可以直接使用 `activate.bat` 运行bot和cqhttp客户端（要求cqhttp客户端与bot在同一级文件夹下），也可以先使用指令 `nb run --file=bot.py` 启动bot，再运行go-cqhttp客户端；
7. 注意，第一次运行go-cqhttp客户端，可能需要扫码登陆；
8. bot成功运行，即刻享受Asoul-bot的各项功能吧！

## 参数配置
`SUPERUSERS : List[str]` 描述超级用户QQ号，是直接控制bot的权限，非群内群主、管理员，如`"123456"`；
`COMMAND_START : List[str]` 描述bot响应命令时的触发符号，如`"/"`、`"."`或`" "`等；

`blacklist : List[str]` 描述bot黑名单成员，如果成员QQ号在黑名单内则不响应，如`"123456"`；
`music : str` 描述点歌插件的app接口，如`"https://xxx.vercel.app"`

`asoul : List[int]` 描述UP主B站UID，可以添加其它UID
`live : List[int]` 描述直播B站房间ID，可以添加其它ID
`imgs : List[int]` 描述表情包UP的B站UID，可以添加其它UID
`tictok : List[int]` 描述抖音UP的B站UID，可以添加其它UID
`slices : List[int]` 描述切片UP的B站UID，可以添加其它UID
`setu_groups : List[int]` 描述涩图的QQ群号，如请求来源的QQ群号不在内则会拒绝请求
`push_groups : List[int]` 描述推送消息的QQ群号，只会向这些群号推送消息
`test_group : str` 描述测试信息发布的群号，只用于技术测试

`assist_path : str` 描述插件的辅助信息路径
`driver_path : str` 描述插件的所用驱动路径
`data_path : str` 描述插件的数据存储路径


## 功能实现


1. 使用方法：@bot然后输入命令，如 `@bot help` 即可唤出帮助菜单；
- 输入关键词：指@bot然后输入的语句中带有关键词即可，如`@bot 有什么功能` 也可以唤出帮助菜单；
- 输入指令：指@bot后必须以“命令+参数”的形式才能触发，如`@bot 冷笑话`才可以获取随机冷笑话， `@bot 来点冷笑话` 并不可以达到这个效果；

2. 已实现功能：
- bot支持黑名单功能，在黑名单内的用户将不会触发bot
- bot支持戳一戳功能，如果bot有管理员权限将会随机禁言
- bot可以选择直播、动态等信息推送的群和关注的用户
- 无需@bot，只需输入任意的BV号、B站视频链接、B站直播间链接将会返回标题、UP主和封面
- 输入指令 “常用/常用功能” 获取常用功能详细介绍\n\
- 输入指令 “注意/注意事项” 获取注意事项\n\
- 输入指令 “游戏” 获取（做到一半的）游戏帮助\n\
- 输入指令 “说/转语音 内容” 进行文字转语音，上限30个字符
- 输入指令 “B站/bili/B站 搜索内容” 进行视频搜索推送
- 输入指令 “emoji表情+emoji表情” 获取emojimix表情
- 输入指令 “点歌/声音/专辑/歌手 搜索内容 第x首” 获取点歌内容，如果不加第x首则默认第1首
- 输入指令 “疯狂星期四” 获取疯狂星期四小作文
- 输入指令 “roll/.r/r xdy” 进行一次掷骰，返回x个y面的骰子点数之和
- 输入指令 “色图/涩图” 获取随机色图
- 输入指令 “猫猫” 获取随机猫猫
- 输入指令 “彩虹屁 主题” 获取彩虹屁小作文
- 输入指令   “冷笑话/笑话” 获取随机冷笑话
- 输入关键词 “运势 版本强势CP名/人物” 获取该人物CP今日运势
- 输入关键词 “日程表” 获取本周日程表
- 输入指令   “实时粉丝数/粉丝数” 获取AS五人+阿草实时粉丝数
- 输入指令   “人品/运势” 获取你今日的运势
- 输入指令   “remake/重开” 获取重开结果
- 输入关键词 “QA/qa” 获取本周QA
- 输入关键词 “午饭/晚饭/夜宵/吃”等 获取你到底吃啥（带学生不吃早饭和下午茶！）
- 输入指令   “小作文” 获取随机小作文
- 输入指令   “狗屁不通 主题” 生成一段狗屁不通的文章
- 输入指令   “概率 事件” 获取某事发生的概率
- 输入指令   “绝绝子 主题” 生成绝绝子小短文
- 输入指令   “匹配 匹配对象” 测试你和ta的匹配程度，或 “匹配 A B”测试A和B的匹配程度
- 输入指令   “表情包” 获取随机表情包（感谢表情包man）
- 输入指令   “切片” 获取随机切片（感谢切片man）
- 推送功能可选开启（请联系管理员）：
    -开播提醒
    -动态发布提醒
    -日程表发布提醒
    -抖音小视频发布提醒


 
## 注意事项
1. 本项目基于AGPL协议开源
2. 本项目的开源、二次使用都应当遵守中华人民共和国的法律法规
3. 本项目的开源、二次使用应当遵守A-SOUL_Official的最新版二创规则声明
4. 本项目的开源、二次使用都应当不包含对其他人的诋毁、拉踩

## 作者及主要贡献者
1. JackFishxxx
2. Avafish

## 参考链接
1. [开源项目代码](https://github.com/JackFishxxx/Asoul-bot)
2. [nonebot2 Document](https://v2.nonebot.dev/)
3. [go-cqhttp Github](https://github.com/Mrs4s/go-cqhttp)
4. [Avafish/Asoul-bot](https://github.com/Avafish/Asoul-bot)
5. [二创规则说明4.0](https://www.bilibili.com/read/cv12242629)
6. [二创规则说明4.0更新](https://www.bilibili.com/read/cv12242629)
7. [emojimix](https://github.com/noneplugin/nonebot-plugin-emojimix)
8. [nonebot-plugin-apscheduler](https://github.com/nonebot/plugin-apscheduler)
9. [网易云音乐API](https://github.com/Binaryify/NeteaseCloudMusicApi)