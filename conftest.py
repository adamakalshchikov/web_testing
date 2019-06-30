from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
import sys


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome" or browser_name is None:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs',
                                        {'intl.accept_languages': request.config.getoption("language")})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", request.config.getoption("language"))
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented".format(browser_name))
        sys.exit(1)
    yield browser
    print("\nquit browser..")
    browser.quit()


