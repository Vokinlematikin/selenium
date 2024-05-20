from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(10)
upload_field = (driver.find_element(By.XPATH, "//input[@type='file']"))
upload_field.send_keys("D:/PYCHARM/hulk.jpg")
#upload_field.send_keys(f"{os.getcwd()}/PYCHARM/hulk.jpg")


time.sleep(10)
driver.close()