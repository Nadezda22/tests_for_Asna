import pytest



def test_log_right_user(browser, authorize_right_user):
    message = 'user has been successfully logged in'
    print(message)


def test_log_in_locked_user(browser, authorize_log_out_user):
    browser.find_element("xpath", '//div[@class="error-message-container error"]')
    error_message = 'Epic sadface: Sorry, this user has been locked out.'
    print(error_message)


def test_log_in_user_to_views(browser, authorize_user_to_views):
    message = 'user with the right to view has been successfully logged in'
    print(message)
