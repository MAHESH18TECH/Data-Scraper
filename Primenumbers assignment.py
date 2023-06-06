#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from parsel import Selector
import pandas as pd
import time
# Launch the Chrome browser
driver = webdriver.Chrome()

driver.get("https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787")
time.sleep(10)

scroll_height = driver.execute_script("return document.documentElement.scrollHeight")
viewport_height = driver.execute_script("return window.innerHeight")

# Define the scrolling increment
scroll_increment = 10  # Adjust the value as needed
#Define the span class
span = driver.find_elements(By.XPATH,'//*[@id="table_id"]/tbody/tr')
for i in span:
    driver.get("https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787")
    time.sleep(20)
    # Perform actions with the element
    i.click()
    description  = driver.find_element(By.XPATH, '//*[@id="current_project"]/div/div[3]/div/table/tbody/tr[3]/td[2]')
    print(description.text)
    Est_value = driver.find_element(By.XPATH,'//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[3]/td[2]')
    print(Est_Value)
    Closing_Date = drver.find_element(By.XPATH,'//*[@id="current_project"]/div/div[2]/div/table/tbody/tr[1]/td[2]')
    print(Closing_Date)

