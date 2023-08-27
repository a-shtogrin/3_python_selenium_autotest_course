import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser1, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser1.get(link)
    browser1.find_element(By.CSS_SELECTOR, "#login_link")