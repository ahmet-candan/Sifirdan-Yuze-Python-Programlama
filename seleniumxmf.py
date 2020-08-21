from selenium import webdriver
import requests 
from bs4 import BeautifulSoup

path = "C:/Users/Lenovo/Desktop/chromedriver"

driver = webdriver.Chrome(executable_path=path)
driver.get("https://www.chrisburkard.com/")
html = driver.execute_script("return decument.documentElement.outerHTML")
sel_soup = BeautifulSoup(html,'html.parser')
print(len(sel_soup.findAll("img")))
