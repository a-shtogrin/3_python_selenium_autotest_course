import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
form = browser.find_element(By.CLASS_NAME, "form-group")
browser.execute_script("return arguments[0].scrollIntoView(true)", form)
time.sleep(3)
button.click()
