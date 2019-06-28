from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
import time


def test_add_to_chart_is_presence(browser: RemoteWebDriver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    button = browser.find_element_by_css_selector("#add_to_basket_form>button")
    time.sleep(10)
    assert button, "Button not found by '#add_to_basket_form>button' selector"
