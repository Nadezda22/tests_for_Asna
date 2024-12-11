import pytest
from selenium import webdriver

users = {
    "user": {"username": "standard_user", "password": "secret_sauce"},
    "locked_user": {"username": "locked_out_user", "password": "secret_sauce"},
    "error_user": {"username": "error_user", "password": "secret_sauce"}}

selected_user = "user"
right_user = users[selected_user]

wrong_user = "error_user"
forbidden_user = users[wrong_user]

log_out_user = "locked_user"
unauthorized_user = users[log_out_user]

test_url = "https://www.saucedemo.com/"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    url = test_url
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def authorize_right_user(browser):
    url = test_url
    browser.get(url)
    login = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Username"]')
    password = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Password"]')
    enter = browser.find_element("xpath", '//input[@data-test="login-button"]//parent::*')

    login.send_keys(right_user["username"])
    password.send_keys(right_user["password"])
    enter.click()


@pytest.fixture
def authorize_forbidden_user(browser):
    url = test_url
    browser.get(url)
    login = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Username"]')
    password = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Password"]')
    enter = browser.find_element("xpath", '//input[@data-test="login-button"]//parent::*')

    login.send_keys(forbidden_user["username"])
    password.send_keys(forbidden_user["password"])
    enter.click()


@pytest.fixture
def authorize_log_out_user(browser):
    url = test_url
    browser.get(url)
    login = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Username"]')
    password = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Password"]')
    enter = browser.find_element("xpath", '//input[@data-test="login-button"]//parent::*')

    login.send_keys(unauthorized_user["username"])
    password.send_keys(unauthorized_user["password"])
    enter.click()
