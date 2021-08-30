from os import path

import nonebot
import bot_config


nonebot.init(bot_config)
# 第一个参数为插件路径，第二个参数为插件前缀（模块的前缀）
nonebot.load_plugins(path.join(path.dirname(__file__), 'bot_plugins'), 'bot_plugins')
nonebot.load_builtin_plugins()

""" # 如果使用 asgi
bot = nonebot.get_bot()
app = bot.asgi """

if __name__ == '__main__':
    nonebot.run()