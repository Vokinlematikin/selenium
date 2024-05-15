from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check

driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/ru/by/login")
#print(type(driver.find_element("id", "loginformsubmit")))
time.sleep(10)
driver.find_element(By.ID, "loginformsubmit").click()
time.sleep(5)
driver.close()