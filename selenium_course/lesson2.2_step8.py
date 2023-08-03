import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'text.txt')           # добавляем к этому пути имя файла

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input_firstname = browser.find_element(By.NAME, "firstname")
    input_lastname = browser.find_element(By.NAME, "lastname")
    input_email = browser.find_element(By.NAME, "email")
    input_firstname.send_keys("Ivan")
    input_lastname.send_keys("Ivanov")
    input_email.send_keys("ivanow@mail.ru")

    button = browser.find_element(By.ID, "file")
    button.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
