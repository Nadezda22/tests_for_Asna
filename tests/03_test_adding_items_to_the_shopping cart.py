def test_delete_delete_one_product(browser, authorize_right_user):
    baby_bodysuit = browser.find_element("xpath", '//div[@class="pricebar"]//button[@name="add-to-cart-sauce-labs-onesie"]')
    baby_bodysuit.click()

    shopping_cart = browser.find_element("xpath", '//div[@class="shopping_cart_container"]')
    shopping_cart.click()

    body_suit = browser.find_element("xpath", '//div[@class="cart_item_label"]//a[@data-test="item-2-title-link"]')
    body_suit.click()

    button_for_delete = browser.find_element("xpath", '//button[@data-test="back-to-products"]')
    button_for_delete.click()

    message = 'product has been removed from the shopping cart'
    print(message)


def test_successful_purchase_of_the_product(browser, authorize_right_user):
    backpack = browser.find_element("xpath", '//div[@class="pricebar"]//button[@name="add-to-cart-sauce-labs-backpack"]')
    backpack.click()

    shopping_cart = browser.find_element("xpath", '//div[@class="shopping_cart_container"]')
    shopping_cart.click()

    button_for_buy = browser.find_element("xpath", '//div[@class="cart_footer"]//button[@data-test="checkout"]')
    button_for_buy.click()

    First_name = browser.find_element("xpath", '//div[@class="checkout_info"]//input[@data-test="firstName"]')
    Last_Name = browser.find_element("xpath", '//div[@class="checkout_info"]//input[@placeholder="Last Name"]')
    credit_card = browser.find_element("xpath", '//div[@class="checkout_info"]//input[@placeholder="Zip/Postal Code"]')
    shop_button = browser.find_element("xpath", '//div[@class="checkout_buttons"]//input[@data-test="continue"]')
    First_name.send_keys('test_name')
    Last_Name.send_keys('test_last_name')
    credit_card.send_keys('85747')
    shop_button.click()

    finish_buy = browser.find_element("xpath", '//div[@class="cart_footer"]//button[@data-test="finish"]')
    finish_buy.click

    message = 'Thank you for your order!'

    print(message)
