import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/redirect_accept.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_window = browser.window_handles[0]

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    second_window = browser.window_handles[1]

    #переключение на другое окно
    browser.switch_to.window(second_window)

    # выбор значения Х на странице
    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    print(x)
    y = calc(x)
    print(y)

    # выбор поля ввода
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


