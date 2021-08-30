from bilibili_api import user
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import nonebot
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

uid = [672346917,672353429,351609538,672328094,672342685,703007996,434334701]
uid_len = len(uid)
rids = [0,0,0,0,0,0,0]
qqgroup = []
qq_noshark = []
qq_len = len(qqgroup)
qq_noshark_len = len(qq_noshark)
bot = nonebot.get_bot()

@nonebot.scheduler.scheduled_job('interval', minutes=3)
async def main():
    t = time.time()
    t = int(t)
    for i in range (0,uid_len):
        u = user.User(uid[i])
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
        dif = (t - ti)/600
        if rid == rids[i]:
            pass
        elif dif > 1:
            pass
        else:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path=r'C:\drivers\chromedriver.exe',chrome_options=chrome_options)
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
            path = r"C:\Users\Administrator\Desktop\luciabot\gocqhttp\data\images\{}.png".format(rid)
            driver.get_screenshot_as_file(path)
            driver.quit()       
            img= Image.open(path)
            cut = img.crop((275,65,910,800))
            cut.save(path)
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
                        "file": "{}.png".format(rid)
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