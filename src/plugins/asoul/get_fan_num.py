# -*- coding: utf-8 -*-
import requests
import json
import time
import os
from nonebot.rule import to_me
from nonebot.adapters import Bot, Event
from nonebot import on_command
from nonebot import require
import nonebot

fan_num = on_command('实时粉丝数',aliases={'粉丝数'}, rule=to_me())

@fan_num.handle()
async def _(bot: Bot, event: Event):
    
    uid_list = bot.config.asoul
    group = int(event.get_session_id().split("_")[1])

    name = ["向晚","贝拉","珈乐","嘉然","乃琳","羊驼"]
    payload = "注意！此功能不应经常使用！\n"
    payload = payload + "{0:{2}>8}{1:{2}>5}".format("当前粉丝", "今日变化", chr(12288))
    
    uid_list = bot.config.asoul

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'asoul.json')
    with open(data_path,'rb') as fp:
        data = json.load(fp)

    i = 0
    for uid in uid_list:
        try:
            bilibili_api = requests.get("http://api.bilibili.com/x/relation/stat?vmid={}".format(uid))  # 访问网址，数据存到变量
        except OSError:
            break
        extracting_json = bilibili_api.text
        python_dictionary = json.loads(extracting_json)
        try:
            fans_num = python_dictionary['data']['follower']
        except TypeError:
            break
        delta_num = fans_num-data[str(uid)]["fans"]
        payload = payload + "\n{0:{3}<4}{1:<10}{2:>+6}".format(name[i], fans_num, delta_num, chr(12288))
        i = i + 1
        time.sleep(0.5)
    await bot.send_group_msg(group_id=group, message=payload)


scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('cron', hour='23', minute='59', second='59', id="update_fan_num")
async def main():

    bot = nonebot.get_bot()
    uid_list = bot.config.asoul

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'asoul.json')
    with open(data_path,'rb') as fp:
        data = json.load(fp)

    for uid in uid_list:
        try:
            bilibili_api = requests.get("http://api.bilibili.com/x/relation/stat?vmid={}".format(uid))  # 访问网址，数据存到变量
        except OSError:
            break
        extracting_json = bilibili_api.text
        python_dictionary = json.loads(extracting_json)
        try:
            fans_num = python_dictionary['data']['follower']
        except TypeError:
            break
        data[str(uid)]["fans"] = fans_num
        time.sleep(0.5)
    
    with open(data_path, 'w') as fp:
        json.dump(data, fp)
