import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/explicit_wait2.html"
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get(link)

try:
    button = browser.find_element(By.ID, "book")
    #ждем пока не появится текст с нужной записью
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

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
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

