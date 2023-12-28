# installing package
from bs4 import BeautifulSoup
import requests
import pandas as pd

#Setting up url Accsess for scrapping
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
response = requests.get(url,headers={'user-Agent':'chrome'})
page = BeautifulSoup(response.text,'html.parser')

#setting anchor point for data Retrival
try:
    main = page.find('table',class_='wikitable sortable')
    table_row_head = main.find_all('th') # type: ignore
    table_header = [row.text.strip() for row in table_row_head]
    db = pd.DataFrame(columns = table_header)
    table_row = main.find_all('tr') # type: ignore
    for value in table_row[1:]:
        column_data = value.find_all('td')
        table_data = [data.text.strip() for data in column_data ]
        length = len(db)
        db.loc[length] = table_data
        #saving the gathered data into a csv file
    db.to_csv(r'D:\PROGGRAMING\codes\python pycharm\demo\MyCodingNinja\project_work\1.csv',index=False)
except Exception as e:
    print(e)