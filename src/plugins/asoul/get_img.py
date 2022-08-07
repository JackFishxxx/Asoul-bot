from bilibili_api import user
import json
import nonebot
import re
import os
from nonebot.plugin import require
import requests
from bs4 import BeautifulSoup

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', hours=12, id="get_img")
async def main():
    bot = nonebot.get_bot()

    uid_list = bot.config.img
    test_group = bot.config.test_group
    
    id_list = []
    img_list = []
    pn = 1

    for uid in uid_list:
        u = user.User(uid)
        while True:
            page = await u.get_articles(pn)
            articles = page['articles']
            art_len = len(articles)
            for i in range(0,art_len):
                id = articles[i]['id']
                id_list.append(id)
            ps = page['ps']
            count = page['count']
            if pn*ps > count:
                break
            else:
                pn = pn + 1
    for cv_id in id_list:
        url = r'https://www.bilibili.com/read/cv' + str(cv_id)
        data = requests.get(url).text
        soup = BeautifulSoup(data, "html.parser", from_encoding="utf-8")
        content = soup.find_all("div", attrs={"id": "article-content"})
        content_soup = BeautifulSoup(str(content[0]), "html.parser", from_encoding="utf-8")
        content_data = content_soup.find_all("img")
        for index in range(len(content_data)):
            if index != 0:
                img = re.sub("//", "", content_data[index]["data-src"])
                img_list.append(img)
    img_path = os.path.join(os.getcwd(),bot.config.assist_path,'img.json')
    img_obj = open(img_path, 'w')
    json.dump(img_list, img_obj)
    await bot.send_group_msg(group_id=test_group, message = 'image updated')