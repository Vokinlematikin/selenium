from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


driver = webdriver.Chrome()
driver.get("https://www.freeconferencecall.com/global/by")
login_button = driver.find_element(By.XPATH, "//a[@id='login-desktop']")
login_button.click()


email_field = driver.find_element(By.XPATH, "//input[@id='login_email']")
email_field.send_keys("Mail@mail.ru")
time.sleep(13)
print(email_field.get_attribute("value"))
email_field.clear()
email_field.send_keys("123456789@mail.ru")
print(email_field.get_attribute("value"))
time.sleep(13)

driver.close()