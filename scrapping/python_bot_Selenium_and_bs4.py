from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests, time, openpyxl
import pandas as pd
try:
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "Top Rated movies"
    print(excel.sheetnames)
    sheet.append(["Name","Year","Age"])
    excel.save('1.xlsx')
    
except Exception as e:
    print(e)
