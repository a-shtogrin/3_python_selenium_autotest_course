from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.FORM_FOR_PRODUCTS), \
            "There are products, but should not be"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), "NO empty text"
