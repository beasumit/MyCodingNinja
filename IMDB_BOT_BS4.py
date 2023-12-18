from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests, time

url = "https://www.imdb.com/chart/top/"
response = requests.get(url,headers={'user-Agent':'chrome/120.0.6099.110'})
response.raise_for_status()
html = response.text 
try:
    data = BeautifulSoup(html,"html.parser")
    main = data.find("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-71ed9118-0 kxsUNk compact-list-view ipc-metadata-list--base")
    titles = main.find_all("li") # type: ignore
    with open("Movie_list_using_bs4.txt","w") as f:
        headers ="Data \n"
        for title in titles:
            name = title.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-43986a27-9 gaoUku cli-title").h3.get_text()
            year = title.find('div',class_="sc-43986a27-7 dBkaPT cli-title-metadata").span.get_text()
            duration = title.find_all('span',class_="sc-43986a27-8 jHYIIK cli-title-metadata-item")[1].get_text()
            link = title.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-43986a27-9 gaoUku cli-title").a["href"]
            f.write(name+'\n')
            f.write(f'Year Released : {year}'+'\n')
            f.write(f'Duration:{duration}'+'\n')
            f.write(f'Link: {url+link}'+'\n')
            f.write("--------------------------------------"+'\n')
    

    f.close()
except Exception as e:
    print(e)