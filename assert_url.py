from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
import pytest_check as check


driver = webdriver.Chrome()
driver.get("https://www.wikipedia.org/")
url = driver.current_url
assert url == "https://www.wikipedia.org/", "Неверная ссылка сайта!"
time.sleep(3)
print('URL страница википедии:', url)

current_title = driver.title
print('Текущий title страницы:', current_title)
assert current_title == "Wikipedia", "Title страницы неверный!"

driver.close()