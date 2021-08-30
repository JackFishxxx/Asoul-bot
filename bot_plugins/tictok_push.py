import requests
import re
import nonebot

urls = [r"https://www.douyin.com/user/MS4wLjABAAAAxOXMMwlShWjp4DONMwfEEfloRYiC1rXwQ64eydoZ0ORPFVGysZEd4zMt8AjsTbyt",r"https://www.douyin.com/user/MS4wLjABAAAAlpnJ0bXVDV6BNgbHUYVWnnIagRqeeZyNyXB84JXTqAS5tgGjAtw0ZZkv0KSHYyhP",r"https://www.douyin.com/user/MS4wLjABAAAAuZHC7vwqRhPzdeTb24HS7So91u9ucl9c8JjpOS2CPK-9Kg2D32Sj7-mZYvUCJCya",r"https://www.douyin.com/user/MS4wLjABAAAA5ZrIrbgva_HMeHuNn64goOD2XYnk4ItSypgRHlbSh1c",r"https://www.douyin.com/user/MS4wLjABAAAAxCiIYlaaKaMz_J1QaIAmHGgc3bTerIpgTzZjm0na8w5t2KTPrCz4bm_5M5EMPy92"]
headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'
    }
qqgroup = []
qq_len = len(qqgroup)
bot = nonebot.get_bot()
@nonebot.scheduler.scheduled_job('interval', minutes=5)
async def main():
    for url in urls:
        r = requests.get(url,headers=headers)
        html = r.text
        html = html.encode()
        h = html.decode('utf-8')
        pattern = re.compile(r'<a href="https://www.douyin.com/video/'+r'\d+')
        n = re.findall(pattern,h)
        new_url = n[3]#置顶有三个
        n_pattern = re.compile(r'https://www.douyin.com/video/'+r'\d+')
        n_n = re.findall(n_pattern,new_url)
        req = requests.get(n_n[0],headers=headers)
        htmll = req.text
        htmll = htmll.encode()
        hh = htmll.decode('utf-8')
        new_pattern = re.compile(r'description" content="'+r'.+'+r'- ',re.U)
        title = re.findall(new_pattern,hh)
        t = title[0]
        t = re.sub(r'description" content="','',t)
        t = re.sub(r'- ','',t)
        name = re.findall(r'- '+r'.+'+r'于',hh,re.U)
        name = str(name[0])
        name = re.sub(r'- ','',name)
        name = re.sub(r'于','',name)
        f = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\{}.txt'.format(name),'r')
        txt = f.read()
        txt = txt.strip()
        if n_n[0] == txt:
            f.close()
        else:
            f.close
            f = open(r'C:\Users\Administrator\Desktop\luciabot\lucia\bot_plugins\assist\{}.txt'.format(name),'w')
            f.write(n_n[0])
            rely = [{
                "type":"text",
                "data":{
                    "text":"来自" + name + '的抖音小视频：\n' + t + '\n' + n_n[0]
                }
            }]
            for i in range(0,qq_len):
                await bot.send_group_msg(group_id=qqgroup[i],message=rely)