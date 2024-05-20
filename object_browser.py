from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


driver = webdriver.Chrome()
driver.set_window_size(1600, 720)
driver.get("https://www.freeconferencecall.com/global/by")

time.sleep(13)

driver.close()