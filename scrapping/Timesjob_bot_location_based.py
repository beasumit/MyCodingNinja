from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import requests, time ,openpyxl

print("Enter The State where you want to work.(PLEASE WRITE THE FIRST LETTER CAPITAL OF THE STATE)")
location_input = input('>')
print(f'Searching for jobs in {location_input}')
try:
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = "Python Job Search"
    sheet.append([" Company Name "," Location "," Skill "," Experience "," Posted ", "Link "])
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
    for i in title:
        posted = i.div.div.div.find('span',class_="sim-posted").get_text().strip()
        if "few" in posted:
            name = i.header.h3.get_text().strip()
            location = i.ul.find_all("li")[1].span.get_text().strip()
            skill = i.find("ul",class_="list-job-dtl clearfix").find_all("li")[1].span.get_text().strip().replace(" ","")
            experience = i.ul.li.get_text().replace('card_travel',' ')
            link = i.header.h2.a["href"]
            if location_input in location:
                    print(f'Company Name : {name}'+"\n")
                    print(f'Company Location : {location}'+"\n")
                    print(f'Skill Required : {skill}'+"\n")
                    print(f'Experience : {experience}'+"\n")
                    print(f'Posted On : {posted}'+"\n")
                    print(f'Link :{link}'+'\n')
                    print("---------------------------------")
                    sheet.append([name,location,skill,experience,posted,link])
    else:           
        print(f'THE END')
    excel.save("Job_based_on_location.xlsx")
    print("File Printed")
except Exception as e:
    print(e)

