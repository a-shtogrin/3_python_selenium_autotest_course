import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def sum(x, y):
    return str(x + y)


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)  # open web site
    # выбор значениq Х и Y на странице
    x_element = browser.find_element(By.ID, "num1")
    y_element = browser.find_element(By.ID, "num2")
    x = int(x_element.text)
    y = int(y_element.text)
    print(f"число {x} и число {y}")
    summa = sum(x, y)

    # выбор списка
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summa)  # ищем сумму в списке

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
