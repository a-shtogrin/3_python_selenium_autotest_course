import math
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from login_password import password, login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('site_number', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_authorisation(browser, site_number):

    try:

        link = f"https://stepik.org/lesson/{site_number}/step/1"
        browser.get(link)

        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "ember33")))
        # button = browser.find_element((By.ID, "ember33"))

        button.click()
        print("--------------------------Кнопка Войти нажата------------------------------")

        # выбор поля ввода
        input_field_login = browser.find_element(By.NAME, "login")
        input_field_password = browser.find_element(By.NAME, "password")
        input_field_login.send_keys(login)
        input_field_password.send_keys(password)

        print("--------------------------Логин и пароль введены в поля-------------------------")

        # Отправляем заполненную форму
        # login_button = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        login_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn")))
        login_button.click()
        print("--------------------------Login кнопка нажата----------------------------------")

        time.sleep(5)

        # Проверяем выполнена ли задача до этого момента
        try:
            again_button = browser.find_element(By.CSS_SELECTOR, "button.again-btn")
            print("--------------------------задача была решена ранее-----------------------")
            again_button.click()
            print("--------------------------кнопка Решить Снова нажата-----------------------")

        except Exception as e:
            print(e)

        time.sleep(5)

        # Вводим ответ в поле
        input_field_answer = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
        answer = math.log(int(time.time()))

        input_field_answer.send_keys(answer)
        print("--------------------------ответ введен в поле---------------------------------")

        time.sleep(5)

        submit_button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")

        submit_button.click()
        print("--------------------------кнопка Отправить нажата------------------------------")

        time.sleep(5)

        check_field = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")
        check_massage = check_field.text
        assert "Correct!" == check_massage, f"Не корректно!! {check_massage}"
        print("--------------------------Ответ Correct!!!-----------------------------------")

    except Exception as e:
        print(f"Проблемы!!!: {e}")




