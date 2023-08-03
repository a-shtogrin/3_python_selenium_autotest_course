import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)  # open web site
    # выбор значения Х на странице
    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text) #Атрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    print(x_element)
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

