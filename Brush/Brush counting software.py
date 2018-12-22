'''
    2017年6月1日22:53:56
    “我行我素”竞赛刷票插件
    主要是用于给自己队伍刷票用的
'''
import requests
import json
import time
import re

# 请求头信息
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Content-Length': '7',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_46cc656d0f576edb23095b27888f2d78=1543156445; PHPSESSID=1kcopcbsp7t6pq9pa0gclqigg5',
    'DNT': '1',
    'Host': 't.dramastar.org',
    'Origin': 'http://t.dramastar.org',
    'Referer': 'http://t.dramastar.org/830.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# post表单网址
url = "http://t.dramastar.org/ajax/add_zan.php"
params = {'tid': ['830']}


def WriteIPadress():
    all_url = []  # 存储IP地址的容器
    # 代理IP的网址

    f = open("IP.txt", 'r')
    all_url = f.readlines()

    return all_url

# 计数器
count = 0
errcount = 0
while count < 1000:
    all_url = WriteIPadress()
    for i in all_url:
        proxies = {"http": 'http://'+i.replace('\n', '')}
        # time.sleep(1)
        try:
            r = requests.post(url=url, data=params,
                              headers=headers, proxies=proxies, timeout=3)
            print(r.text)
            if(r.json()['result'] == True):
                count += 1
                print("成功投票%d次！" % (count))
            print(r.json())
        except Exception as reason:
            print("错误原因是：", reason)
            errcount += 1
            if (errcount > 900):
                break
    break