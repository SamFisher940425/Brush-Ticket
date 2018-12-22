#coding:utf-8
'''
    2017年6月1日22:53:56
    “我行我素”竞赛刷票插件
    主要是用于给自己队伍刷票用的
'''
import json
import time
import asyncio
import re
import aiohttp

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
    'Referer': 'http://t.dramastar.org/127.html',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    #'X-Requested-With': 'XMLHttpRequest'
}

# post表单网址
url = "http://t.dramastar.org/ajax/add_zan.php"
params = {'tid': '127'}


def WriteIPadress():
    all_url = []  # 存储IP地址的容器
    # 代理IP的网址

    f = open("ip.txt", 'r')
    for i in range(51):
        fx = open('ip'+str(i)+'.txt', 'w')
        for j in range(306):
            lines = f.readline()
            fx.write(lines)
        fx.close()
    # all_url = f.readline()

    return all_url

# 计数器
count = [0]
allcc=0
errcount = [0]
all_url = WriteIPadress()

async def vo(i):
    purl = []
    ccc = 0
    ff = open('ip'+str(i)+'.txt','r')
    purl = ff.readlines()
    # print(purl)
##    try:    
    for uu in purl:       
        proxies = 'http://'+uu.replace('\n', '')        
        ccc+=1
        print(proxies,ccc,i)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url=url, data=params,headers=headers, proxy=proxies, timeout=20) as r:
                    c=await r.json(content_type='text/html')
                    if(c['result'] == True):
                        count[0] += 1
                        print("成功投票%d次！" % (count[0]))
                    #print(r.json())        
        except Exception as reason:
            print("错误原因是：", reason,i)
            errcount[0] += 1
##    except Exception as reason:
##        print("错误原因是：", reason,i)


loop = asyncio.get_event_loop()
tasks = [vo(i) for i in range(51)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()








