import urllib.request
import re
from bs4 import BeautifulSoup

fx = open('info.txt', 'w')

focus = [83, 127, 838, 476, 689, 179, 842, 830]

for i in range(1, 863):  # focus:
    
    url = 'http://t.dramastar.org/'+str(i)+'.html'
    res = urllib.request.urlopen(url, timeout=10)
    content = res.read()
    soup = BeautifulSoup(content, 'html.parser')
    v = soup.find(class_='teacher_info')
    c = v.find_all('li')
    sss = c[3].get_text()
    num_zan = re.findall(r'\d+', sss)[0]
    if int(num_zan) > 10000:
        print(i, sss)
        fx.write(str(i) + ':' + str(sss) + '\n')

fx.close()
