from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check
driver = webdriver.Chrome()
driver.get("https://hyperskill.org/tracks")
print(len(driver.find_elements(By.CLASS_NAME, "nav-link")))
time.sleep(10)
driver.find_elements(By.CLASS_NAME, "nav-link")[2].click()

#driver.find_element(By.ID, "loginformsubmit").click()
time.sleep(5)
driver.close()

#elements = ["one", "two", "three"]
#print(elements[1])

