import json
from bilibili_api import user
from pydantic.types import UUID1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import nonebot
from selenium.webdriver.common.action_chains import ActionChains
import cv2
from nonebot import require

rids = [0,0,0,0,0,0,0]

obj = open(r'.\global.json','rb')
data = json.load(obj)
qqgroup = data['all']
qq_noshark = data['no_shark']

uid_all = data["asoul_uid"] + data["shark_uid"]
uid_noshark = data["asoul_uid"]

uid_all_len = len(uid_all)
uid_noshark_len = len(uid_noshark)

qq_len = len(qqgroup)
qq_noshark_len = len(qq_noshark)

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', minutes=10, id="get_dynamic")
async def main():
    bot = nonebot.get_bot()
    t = time.time()
    t = int(t)
    for i in range (0,uid_all_len):
        u = user.User(uid_all[i])
        global rids   
        page = await u.get_dynamics(0)
        cards = page['cards']
        card = cards[0]
        desc = card['desc']
        rid = desc['dynamic_id']
        ti = desc['timestamp']
        usr_pro = desc['user_profile']
        info = usr_pro['info']
        uname = info['uname']
        ti = int(ti)
        dif = (t - ti)/600  # 10 min
        if rid == rids[i]:
            pass
        elif dif > 6:
            pass
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path=r'.\src\drivers\chromedriver.exe',chrome_options=chrome_options)
            url = r"https://t.bilibili.com/" + str(rid)
            driver.get(url)
            time.sleep(2)
            driver.set_window_size(1200, 800)
            action = ActionChains (driver)
            action.move_by_offset(656,96).perform()
            time.sleep(0.5)
            actions = ActionChains (driver)
            actions.move_by_offset(-300,0).perform()
            time.sleep(3)
            path = r".\src\data\images\{}.png".format(rid)
            driver.get_screenshot_as_file(path)
            driver.quit()       
            img = cv2.imread(path)
            cut = img[70:730, 300:900] #change the size here
            cv2.imwrite(path, cut)
            rely =[
                {
                "type": "text",
                "data": {
                    "text": "来自" + uname + "的动态：\n" + url + '\n'
                    }
                },
                {
                    "type": "image",
                    "data": {
                        "file": r"C:\Users\JackFish\Desktop\Github\Asoul-bot\src\data\images\{}.png".format(rid)
                    }
                }]
            if i == 6:
                for j in range(0,qq_len):
                    rids[i] = rid
                    await bot.send_group_msg(group_id=qqgroup[j],message=rely)
            else:
                for k in range(0,qq_len):
                    rids[i] = rid
                    await bot.send_group_msg(group_id=qqgroup[k],message=rely)
                for m in range(0,qq_noshark_len):
                    rids[i] = rid
                    await bot.send_group_msg(group_id=qq_noshark[m],message=rely)