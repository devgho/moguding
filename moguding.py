import requests
import json


def post_days(body, year="2003"):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
        "sign": "2334a5c4196bc2a63419ea17e4d5386b",
        "sec-fetch-dest": "empty",
        "authority": "api.moguding.net:9000",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "authorization": "eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJtb2d1ZGluZy11c2VyIiwic3ViIjoie1wibG9naW5UeXBlXCI6XCJ3ZWJcIixcInVzZXJJZFwiOjEwMzEzNDk1Mn0iLCJhdWQiOiJtb2d1ZGluZyIsImV4cCI6MTk2NjY3OTA3NywibmJmIjoxNjUxMDU4OTc3LCJpYXQiOjE2NTEwNTk4Nzd9.cgUZIm94xNrZSzhZ-K18YL8kH1qLJxkTgal2TH37h-28yz61lQxxPkA3lAdC2Admen0pppjc_R2l4xb3cCW_oQ",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://pra.gongxueyun.com",
        "referer": "https://pra.gongxueyun.com/",
        "rolekey": "student",
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"',
        "sec-ch-ua-mobile": "?0",
        'sec-ch-ua-platform': '"Windows"'
    }
    #日报
    post_d = {
        "t": "52C4D30366A4CF1DDD15E5002C77D326",
        "attachments": "",
        "attachmentList": [],
        "title": "日报",
        "content": body,
        "planId": "c45e697ccd6a3972c6018d6ba0d7c69b",
        "reportType": "day"
    }
    #周报
    post_w = {
            "t": "6AB130FD55C316C06940424835F08BAE",
            "attachments": "",
            "attachmentList": [], "title": "周记",
            "content": body,
            "planId": "c45e697ccd6a3972c6018d6ba0d7c69b", "reportType": "week", "weeks": f"第{year}周",
            "startTime": f"{year}-04-19 00:00:00", "endTime": f"{year}-04-25 23:59:59"
    }
    res = requests.post("https://api.moguding.net:9000/practice/paper/v2/save", headers=headers, json=post_d)
    # res = requests.post("https://api.moguding.net:9000/practice/paper/v2/save", headers=headers, json=post_w) #周报
    print(res)


days = open("days/cDay.json", "r", encoding="utf8")
dt = json.load(days)
for i in dt['data']:
    if i == 0:
        break
    post_days(i['txt'])
days.close()

# year = 1990
# weeks = open("week/week2.json", "r", encoding="utf8") #周报
# dt = json.load(weeks)
# for i in dt['data']:
#     post_days(i['txt'], str(year))
#     year += 1
# weeks.close()
