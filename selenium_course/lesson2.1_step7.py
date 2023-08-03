import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)  # open web site
    # выбор значения Х на странице
    x_element = browser.find_element(By.ID, "treasure")
    x = float(x_element.get_attribute("valuex"))
    print(x_element.get_attribute("valuex"))
    print(type(x_element.get_attribute("valuex")))
    print(x)
    y = calc(x)

    #выбор поля ввода
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    #выбор чекбокса
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    #выбор радиобаттон
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

