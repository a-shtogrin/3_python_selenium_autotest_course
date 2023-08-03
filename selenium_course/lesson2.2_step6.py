import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = " https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)  # open web site
    # выбор значения Х на странице
    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    print(x)
    y = calc(x)
    print(y)

    #скролл страницы
    form = browser.find_element(By.CLASS_NAME, "form-group")
    browser.execute_script("return arguments[0].scrollIntoView(true)", form)

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
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    time.sleep(10)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

