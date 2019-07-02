from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_chart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CHART)
        button.click()

    def check_navigation_panel(self):
        panel_text = self.browser.find_element(*ProductPageLocators.NAV_PANEL).text
        assert panel_text.endswith(self.get_item_name()), "Names are different"

    def verify_success_msg(self, text_expected):
        msg = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        # pdb.set_trace()
        assert msg.text == f"{text_expected} был добавлен в вашу корзину.", "Message don`t match with expected"
        # assert msg.text.startswith(text_expected), "Message don`t match with expected"

    def verify_cart_cost(self, cost_expected):
        elem = self.browser.find_element(*ProductPageLocators.CART_COAST)
        cost = elem.text.split(' ')[4]
        assert cost == cost_expected, "Cost of item and cost of cart are difference"

    def get_item_price(self):
        elem = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        price = elem.text.split()[0]
        return price

    def get_item_name(self):
        elem = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        name = elem.text
        return name

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but not should be"

    def should_element_disappeared(self, *locator, timeout=None):
        if timeout:
            assert self.is_disappeared(*locator, timeout=timeout), 'Element isn`t disappeared, but should be'
        else:
            assert self.is_disappeared(*locator), 'Element isn`t disappeared, but should be'

