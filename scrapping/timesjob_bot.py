from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import requests, time ,openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Python Job Search"
sheet.append([" Company Name "," Location "," Skill "," Experience "," Posted "," Link "])
try:
    url = "https://www.timesjobs.com/"
    driver = webdriver.Chrome()
    driver.get(url)
    input_val = "Python"
    driver.find_element(By.CLASS_NAME,"browser-default").send_keys(input_val)
    driver.find_element(By.XPATH,"//*[(@class = 'waves-effect waves-light btn')]").click()
    scrap_url = driver.current_url
    resposne = requests.get(scrap_url,headers = {'user-Agent':'chrome/120.0.6099.110'})
    main = BeautifulSoup(resposne.text,"html.parser")
    title = main.find_all("li",class_="clearfix job-bx wht-shd-bx")
    pandap = []
    for i in title:
        name = i.header.h3.get_text().strip()
        location = i.ul.find_all("li")[1].span.get_text().strip()
        skill = i.find("ul",class_="list-job-dtl clearfix").find_all("li")[1].span.get_text().strip().replace(" ","")
        experience = i.ul.li.get_text().replace('card_travel',' ')
        posted = i.div.div.div.find('span',class_="sim-posted").get_text().strip()
        link = i.header.h2.a["href"]
        # print(f'Company Name : {name}'+"\n")
        # print(f'Company Location : {location}'+"\n")
        # print(f'Skill Required : {skill}'+"\n")
        # print(f'Experience : {experience}'+"\n")
        # print(f'Posted On : {posted}'+"\n")
        # print(f'Link :{link}'+'\n')
        # print("---------------------------------")
        info ={'Name':name,
                'Company Location':location,
                'Skill Required' : skill,
                'Experience' : experience,
                'Posted On' : posted,
                'Link' : link}
        pandap.append(info)
        sheet.append([name,location,skill,experience,posted,link])
    data_set = pd.DataFrame(pandap)
    data_set.to_excel('Movie_data_set.xlsx')
except Exception as e:
    print(e)

excel.save("job_search_Result.xlsx")
print("File Printed")
