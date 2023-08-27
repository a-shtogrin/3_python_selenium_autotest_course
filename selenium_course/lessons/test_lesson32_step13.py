import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link_1 = "http://suninjuly.github.io/registration1.html"
link_2 = "http://suninjuly.github.io/registration2.html"


class Selectors(unittest.TestCase):
    def test_1(self):
        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link_1)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("Petrov@mail.ru")

        time.sleep(1)
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"The text is wrong: {welcome_text}")

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_2(self):

        self.browser = webdriver.Chrome()
        browser = self.browser
        browser.get(link_2)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
        input3.send_keys("Petrov@mail.ru")

        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"The text is wqong: {welcome_text}")

        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
