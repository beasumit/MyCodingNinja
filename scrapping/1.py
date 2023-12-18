from bs4 import BeautifulSoup
import requests
import time
from random import randint

dct = {}
for i in range(1,202,50):
    res = requests.get("https://www.imdb.com/search/title?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start="+str(i)+"&ref_=adv_nxt")
    data = BeautifulSoup(res.text,"html.parser")
    tags = data.find_all('div',class_='lister-item')
    for j in tags:
        if j.find('span',class_='runtime'):
            head = j.find('h3',class_='lister-item-header')
            dur = j.find('span',class_='runtime')
            t= int(dur.text.strip().split(' ')[0])
            dct[head.a.string] = t
    time.sleep(randint(0,3))
maxdur = -1
maxnum = 0
for k,v in dct.items():
    if v>maxdur:
        maxdur = v
        maxname = k
print(maxname, maxdur)