import nonebot
from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import re
from selenium import webdriver
import time

bot = nonebot.get_bot()
@on_command('识图')
async def _(session: CommandSession):
    eve = session.event
    msg = eve['message']
    url = re.findall(r'http'+r'.+'+r']',str(msg))
    url = re.sub(']','',url[0])
    driver = webdriver.Chrome(executable_path=r'C:\drivers\chromedriver.exe')
    bd_url = r'https://graph.baidu.com/pcpage/index?tpl_from=pc'
    driver.get(bd_url)
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[7]/div/span[1]/input").clear()
    driver.find_element_by_xpath("/html/body/div/div/div[1]/div[7]/div/span[1]/input").send_keys(url)
    search = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[7]/div/span[2]")
    search.click()
    time.sleep(3)
    page_url = driver.current_url
    driver.quit()
    s = re.findall(r'http'+r'.+'+r'f=all',page_url)
    await session.send(message=str(s[0]))