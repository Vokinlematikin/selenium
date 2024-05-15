from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
time.sleep(5)
driver.get("https://yandex.by/mail")
time.sleep(5)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(2)
driver.close()