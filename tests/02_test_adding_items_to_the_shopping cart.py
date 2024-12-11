def test_add_one_item_to_shopping_cart(browser, authorize_right_user):
    browser.find_element("xpath", '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button_for_Sauce_Labs_Backpack = browser.find_element("xpath", '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button_for_Sauce_Labs_Backpack.click
    message = 'product "Sauce Labs Backpack" has been added to the cart'
    print(message)


def test_add_some_items_to_shopping_cart(browser, authorize_right_user):
    list_items = browser.find_elements("xpath", '//div[@class="inventory_list"]')

    for item in list_items:
        add_button = browser.find_element("xpath", '//button[@class="btn btn_primary btn_small btn_inventory "]')
        add_button.click()
        message = 'all products have been added to the cart'
    print(message)


def test_add_items_to_shopping_cart_for_user_to_views(browser, authorize_user_to_views):
    browser.find_element("xpath", '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button_Fleece_Jacket = browser.find_element("xpath", '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_button_Fleece_Jacket.click
    message = 'product "Fleece_Jacket" has been added to the cart'
    print(message)
