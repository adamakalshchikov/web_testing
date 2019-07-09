from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def cart_should_be_empty(self):
        try:
            self.browser.find_element(*CartPageLocators.BASKET_SUMMARY)
            return False
        except NoSuchElementException:

            return True

    def should_be_emtpy_cart_text_presented(self):
        p_elem = self.browser.find_element(*CartPageLocators.EMPTY_MSG)
        msg = p_elem.text.split('.')[0]
        assert msg == 'Your basket is empty', 'There is no "Your basket is empty" message'
