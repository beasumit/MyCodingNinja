from selenium import webdriver
from selenium.webdriver.chrome.service import service
service = service(executable_path = "C:\Users\bensu\Desktop\COding_ninja_classes\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service = service)
x = driver.get('https://www.google.com')
print(x)