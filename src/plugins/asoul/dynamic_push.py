import json
import time
import os
import cv2
from nonebot import require
from bilibili_api import user
import nonebot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

scheduler = require("nonebot_plugin_apscheduler").scheduler

@scheduler.scheduled_job('interval', minutes=10, id="get_dynamic")
async def main():

    bot = nonebot.get_bot()
    uid_list = bot.config.asoul
    push_groups = bot.config.push_groups

    assist_path = bot.config.assist_path
    data_path = os.path.join(os.getcwd(), assist_path, 'asoul.json')
    with open(data_path,'rb') as fp:
        asoul = json.load(fp)

    for uid in uid_list:
        u = user.User(uid)
        page = await u.get_dynamics(0)
        dynamic_id = page['cards'][0]['desc']['dynamic_id']
        dynamic_type = page['cards'][0]['desc']['type']
        uname = page['cards'][0]['desc']['user_profile']['info']['uname']

        saved_id = asoul[str(uid)]["dynamic"]["id"]
        
        # type: 1:转发    4:原创    8:视频
        if dynamic_type != 1 and dynamic_id != saved_id:

            chrome_options = Options()
            chrome_options.add_argument('--headless')
            mobileEmulation = {'deviceName':'iPhone X'}
            chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
            driver_path = os.path.join(os.getcwd(), bot.config.driver_path, "chromedriver.exe")
            driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
            url = r"https://m.bilibili.com/dynamic/" + str(dynamic_id)
            driver.get(url)
            time.sleep(2)
            dynamic_path = os.path.join(os.getcwd(), bot.config.data_path, "dynamics", "{}.png".format(dynamic_id))
            driver.get_screenshot_as_file(dynamic_path)
            driver.quit()       
            img = cv2.imread(dynamic_path)
            cut = img[136:-290,:,:] #change the size here
            cv2.imwrite(dynamic_path, cut)

            # update
            with open(data_path, 'w') as fp:
                asoul[str(uid)]["dynamic"]["id"] = dynamic_id
                asoul[str(uid)]["dynamic"]["path"] = dynamic_path
                json.dump(asoul, fp)

            reply = "来自{}的动态：\n{}\n[CQ:image,file=file:///{}]".format(uname, url, dynamic_path)

            for push_group in push_groups:
                await bot.send_group_msg(group_id=push_group,message=reply)
        
        elif dynamic_type == 1 and dynamic_id != saved_id:
            dynamic_path = os.path.join(os.getcwd(), bot.config.data_path, "dynamics", "{}.png".format(dynamic_id))
            with open(data_path, 'w') as fp:
                asoul[str(uid)]["dynamic"]["id"] = dynamic_id
                asoul[str(uid)]["dynamic"]["path"] = dynamic_path
                json.dump(asoul, fp)
        
        else:
            pass
