import pytest
from selenium import webdriver

users = {
    "user": {"username": "standard_user", "password": "secret_sauce"},
    "log_out_user": {"username": "locked_out_user", "password": "secret_sauce"},
    "user_to_view": {"username": "visual_user", "password": "secret_sauce"}}

# пользоватей с обычной авторизацией
selected_user = "user"
right_user = users[selected_user]

# заблокированный пользователь
forbidden_user = "log_out_user"
unauthorized_user = users[forbidden_user]

# пользователь с правом просмотра
user_for_view = "user_to_view"
user_to_views = users[user_for_view]

# ссылка приложения
test_url = "https://www.saucedemo.com/"


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    url = test_url
    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.quit()


# фикстура для авторизации пользователя с корректным логином и паролем
@pytest.fixture
def authorize_right_user(browser):
    url = test_url
    browser.get(url)
    login = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Username"]')
    password = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Password"]')
    enter = browser.find_element("xpath", '//div[@class="login-box"]//input[@type="submit"]')

    login.send_keys(right_user["username"])
    password.send_keys(right_user["password"])
    enter.click()


# фикстура для авторизации заблокированного пользователя
@pytest.fixture
def authorize_log_out_user(browser):
    url = test_url
    browser.get(url)
    login = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Username"]')
    password = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Password"]')
    enter = browser.find_element("xpath", '//div[@class="login-box"]//input[@type="submit"]')

    login.send_keys(unauthorized_user["username"])
    password.send_keys(unauthorized_user["password"])
    enter.click()


# фикстура для авторизации пользователя с правом просмотра
@pytest.fixture
def authorize_user_to_views(browser):
    url = test_url
    browser.get(url)
    login = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Username"]')
    password = browser.find_element("xpath", '//div[@class="form_group"]//input[@placeholder="Password"]')
    enter = browser.find_element("xpath", '//div[@class="login-box"]//input[@type="submit"]')

    login.send_keys(user_to_views["username"])
    password.send_keys(user_to_views["password"])
    enter.click()
