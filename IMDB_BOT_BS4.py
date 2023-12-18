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
    print(data)
except Exception as e:
    print(e)