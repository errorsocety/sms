import requests, json
from bs4 import BeautifulSoup
from instabot import Bot

bot = Bot(follow_delay=0)
bot.login(username="nz_nin80", password="kirkir")
cookie = "_ga=GA1.2.1956545561.1632139719; _gid=GA1.2.867999647.1632139719; _ym_uid=1632139720321949234; _ym_d=1632139720; _ym_isad=2; _ym_visorc=w;"
cs = "YII_CSRF_TOKEN=2b929e86aea36b76545aa33205d75b2ecbeb7da9s%3A88%3A%22SDBMeDZ2VHJ6RERkM2g3ZDR2SUNGRTBDZHN-bUNvWktBaW-MfqUBHZNbSRazDWwoG8xOVRr7wftsbWmbpRwzYg%3D%3D%22%3B;"

def follow(id, s):
    h = {
    "Host": "getlike.io",
    "accept": "application/json, text/javascript, */*; q\u003d0.01",
    "x-requested-with": "XMLHttpRequest",
    "save-data": "on",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6,ar;q\u003d0.5",
    "cookie": cookie
    }
    r = s.get("https://getlike.io/tasks/do_m/"+id+"/", headers=h)
    user = json.loads(r.text)["url_to_redirect"].split("/")[3]
    bot.follow(user)
    ch = {
    "Host": "getlike.io",
    "content-length": "137",
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "save-data": "on",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "origin": "https://getlike.io",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6,ar;q\u003d0.5",
    "cookie": cookie
    }
    cd = "id="+id+"&count=1&bot_check=1&"+cs
    cr = s.post("https://getlike.io/tasks/check/", headers=ch, data=cd)
    print(cr.text)

def get_list():
    s = requests.Session()
    h = {
    "Host": "getlike.io",
    "save-data": "on",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q\u003d0.9,image/webp,image/apng,*/*;q\u003d0.8,application/signed-exchange;v\u003db3;q\u003d0.9",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6,ar;q\u003d0.5",
    "cookie": cookie
    }
    r = s.get("https://getlike.io/tasks/instagram/subscribe/", headers=h, data=cs) 
    soup = BeautifulSoup(r.text, features="html.parser")
    list = soup.find_all("article", {"class": "panel-group task_item"})
    for i in list:
        try:
            follow(i.get("id").replace("task-item-", ""), s)
        except:
            print("err!")


while True:
    get_list()
