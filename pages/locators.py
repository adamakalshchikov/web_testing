from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ItemPageLocators(object):
    ADD_TO_CHART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
