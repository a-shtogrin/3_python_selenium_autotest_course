import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_is_there_cart_button(browser):

    browser.get(link)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    cart_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                  "button.btn-add-to-basket")))
    print(f"Текст на кнопке: '{cart_button.text}'")

    assert cart_button

    time.sleep(5)
