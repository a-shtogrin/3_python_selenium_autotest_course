from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//div[contains(@class, 'basket-mini')]//a")


class BasketPageLocators:
    FORM_FOR_PRODUCTS = (By.XPATH, "//form[@id='basket_formset']")
    EMPTY_TEXT = (By.XPATH, "//div[@id='content_inner']//p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    SUB_STRING = "login"


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")

    PRODUCT_IN_BASKET_ALERT = (By.CSS_SELECTOR, "div#messages > div.alert-success:nth-child(2)")
    BASKET_COST_ALERT = (By.CSS_SELECTOR, "div.alert-info")

    PRODUCT_PRICE_IN_ALERT = (By.CSS_SELECTOR, "div.alert-info > div p strong")
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, "div#messages > div.alert-success:nth-child(1) > div >strong")

    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-success')][1]")


