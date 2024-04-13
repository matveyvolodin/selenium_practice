import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def chrome_options():
    options = Options()
    options.add_argument('--headless')
    return options


@pytest.fixture()
def browser(chrome_options):
    browser = webdriver.Chrome(options=chrome_options)
    # browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

