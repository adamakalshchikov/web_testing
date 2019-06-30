from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def add_to_chart(self):
        button = self.browser.find_element(*ItemPageLocators.ADD_TO_CHART)
        button.click()

    def verify_success_msg(self, text_expected):
        msg = self.browser.find_element(*ItemPageLocators.SUCCESS_MSG)
        assert text_expected in msg.text, "Message don`t match with expected"

    def verify_cart_cost(self, cost_expected):
        cost = self.browser.find_element(*ItemPageLocators.CART_COAST).text.split(' ')[4]
        assert cost == cost_expected, "Cost of item and cost of cart are difference"

    def get_item_price(self):
        elem = self.browser.find_element(*ItemPageLocators.ITEM_PRICE)
        price = elem.text.split()[0]
        return price

    def get_item_name(self):
        elem = self.browser.find_element(*ItemPageLocators.ITEM_NAME)
        name = elem.text
        return name
