from selenium_course.pages.base_page import BasePage
from selenium_course.pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def send_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_product_in_basket(self):
        self.should_be_product_in_basket_alert()
        self.should_be_basket_cost_alert()
        self.should_be_product_price_in_alert()
        self.should_be_product_name_in_alert()

    def should_be_product_in_basket_alert(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_BASKET_ALERT), "NO Product_in_basket message"

    def should_be_basket_cost_alert(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_ALERT), "NO basket_cost message"

    def should_be_product_price_in_alert(self):
        print("PRODUCT_PRICE:", self.get_text_from_tag(*ProductPageLocators.PRODUCT_PRICE))
        print("PRODUCT_PRICE_IN_ALERT:", self.get_text_from_tag(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT))
        assert self.get_text_from_tag(*ProductPageLocators.PRODUCT_PRICE) == \
               self.get_text_from_tag(*ProductPageLocators.PRODUCT_PRICE_IN_ALERT), "WRONG product price in alert"

    def should_be_product_name_in_alert(self):
        print("PRODUCT_NAME:", self.get_text_from_tag(*ProductPageLocators.PRODUCT_NAME))
        print("PRODUCT_NAME_IN_ALERT:", self.get_text_from_tag(*ProductPageLocators.PRODUCT_NAME_IN_ALERT))
        assert self.get_text_from_tag(*ProductPageLocators.PRODUCT_NAME) == \
               self.get_text_from_tag(*ProductPageLocators.PRODUCT_NAME_IN_ALERT), "WRONG product name in alert"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappear, but should be"


