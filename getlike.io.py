import requests, json
from bs4 import BeautifulSoup
from instabot import Bot

bot = Bot(follow_delay=0)
bot.login(username="nz_nin80", password="kirkir")
cookie = "__cfduid=d0cc5b1ac4addf177d6e44541b5e8712d1608809047;_ym_uid=1608809048765617939;_ym_d=1608809048;_ga=GA1.2.1319366106.1608809048;_gid=GA1.2.240043241.1608809048;_ym_isad=2;did=a6baafa454cb7a067a598ea7cfc38bc66f4cf2das%3A36%3A%227cc63943-9b67-41de-b95d-b041bbe650a6%22%3B;_ym_hostIndex=0-1%2C1-0;85b6c6296511b0f7fd762e33cb7fdc12=a210c650db21c4c76b836c8d4e2103b7840b85f8s%3A226%3A%229d699fba9297a660da6e24ccc3794dda08b2dfe7a%3A4%3A%7Bi%3A0%3Bs%3A6%3A%22504424%22%3Bi%3A1%3Bs%3A9%3A%22mr0sploit%22%3Bi%3A2%3Bi%3A31536000%3Bi%3A3%3Ba%3A3%3A%7Bs%3A2%3A%22id%22%3Bs%3A6%3A%22504424%22%3Bs%3A4%3A%22name%22%3Bs%3A9%3A%22mr0sploit%22%3Bs%3A4%3A%22auth%22%3Bs%3A50%3A%22215435f527dc95093f7b19234314b9eb3722674aa6878ef68f%22%3B%7D%7D%22%3B;PHPSESSID=19051cd064857723038bd0e8aa92a3f9;YII_CSRF_TOKEN=29e3b321c9c5c13e2d53dbf2f3541dab796d1a9cs%3A88%3A%22UmpSWmtaZXdSTWZJNWh5dnBsYmxOYzMzczhuYjcyV0uv_ULPRPufNQ4R1QahV7OGqSu2BnxJamfsCAcD9q6sSQ%3D%3D%22%3B;_ym_visorc_65242138=w;_gat=1"
cs = "YII_CSRF_TOKEN=29e3b321c9c5c13e2d53dbf2f3541dab796d1a9cs%3A88%3A%22UmpSWmtaZXdSTWZJNWh5dnBsYmxOYzMzczhuYjcyV0uv_ULPRPufNQ4R1QahV7OGqSu2BnxJamfsCAcD9q6sSQ%3D%3D%22%3B"

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
