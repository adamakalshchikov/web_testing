from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators(object):
    ADD_TO_CHART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div .alert:nth-child(1) > div')
    CART_COAST = (By.CSS_SELECTOR, 'div .alert:nth-child(3) > div')
    ITEM_NAME = (By.CSS_SELECTOR, 'div .col-sm-6.product_main > h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div .col-sm-6.product_main > p.price_color')
    NAV_PANEL = (By.CSS_SELECTOR, 'ul.breadcrumb')
