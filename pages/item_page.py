from .base_page import BasePage
from .locators import ItemPageLocators


class ItemPage(BasePage):
    def add_to_chart(self):
        button = self.browser.find_element(*ItemPageLocators.ADD_TO_CHART)
        button.click()
