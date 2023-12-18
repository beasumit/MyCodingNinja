from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests, time
try:
    url = "https://www.imdb.com/chart/top/"
    # web = requests.get(url,headers={'user-Agent':'Chrome/120.0.6099.109'})
    # web.raise_for_status()
    # html = web.text
    driver = webdriver.Chrome()
    driver.get(url)
    title = driver.find_elements(By.XPATH,"//*[(@class = 'ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-43986a27-9 gaoUku cli-title')]/a/h3")
    year = driver.find_elements(By.XPATH,"//*[(@class = 'sc-43986a27-8 jHYIIK cli-title-metadata-item')][1]")
    duration = driver.find_elements(By.XPATH,"//*[(@class = 'sc-43986a27-8 jHYIIK cli-title-metadata-item')][2]")
    rating = driver.find_elements(By.XPATH,"//*[(@class = 'ipc-rating-star--voteCount')]")
    # print(rating.text)
    with open("movie.docs" ,"w") as f:
        headers = "Name \n"
        for i,j,k,l in zip(title,year,duration,rating):
            f.write(f'{i.get_attribute("innerHTML")}'+"\n")
            f.write(f'Released in: {j.get_attribute("innerHTML")}'+'\n')
            f.write(f'Duration: {k.text}'+'\n')
            f.write(f'Rating: {l.text}'+'\n')
            f.write("-----------------------------------------------"+'\n')
            
    f.close()
    # data = BeautifulSoup(html,"html.parser")
    # main = data.find_all("li",class_='ipc-metadata-list-summary-item sc-3f724978-0 enKyEL cli-parent')
    # title = data.div
    # print(title)
except Exception as e:
    print(e)