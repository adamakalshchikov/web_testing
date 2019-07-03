from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.CSS_SELECTOR, "span > .btn:not(.dropdown-toggle)")
    NAV_PANEL = (By.CSS_SELECTOR, 'ul.breadcrumb')


class LoginPageLocators(BasePageLocators):
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators(BasePageLocators):
    ADD_TO_CHART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div .alert:nth-child(1) > div')
    CART_COAST = (By.CSS_SELECTOR, 'div .alert:nth-child(3) > div')
    ITEM_NAME = (By.CSS_SELECTOR, 'div .col-sm-6.product_main > h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div .col-sm-6.product_main > p.price_color')


class CartPageLocators(BasePageLocators):
    EMPTY_MSG = (By.CSS_SELECTOR, "#content_inner>p")
    ITEM_TO_BY_NOW_HEADER = (By.CSS_SELECTOR, "#content_inner h2.col-sm-6")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-primary")
    ORDER_TOTAL_MARK = (By.CSS_SELECTOR, "table.table-condensed th.total>h3")
    BASKET_SUMMARY = (By.ID, 'basket_formset')
