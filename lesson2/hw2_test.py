import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from data import *
from locators import *

# Authorisation using correct data (standard_user, secret_sauce)
def test_auth_positive(browser):
    browser.get(Urls.base_url)
    browser.find_element(By.ID, AuthPageLocators.username_field).send_keys(User.pos_username)
    browser.find_element(By.ID, AuthPageLocators.password_field).send_keys(User.pos_password)
    browser.find_element(By.ID, AuthPageLocators.login_button).click()
    assert browser.current_url == Urls.catalog_url, 'url does not match'
    # time.sleep(2)


# Authorisation using incorrect data (user, user)
def test_auth_negative(browser):
    browser.get(Urls.base_url)
    browser.find_element(By.ID, AuthPageLocators.username_field).send_keys(User.neg_username)
    browser.find_element(By.ID, AuthPageLocators.password_field).send_keys(User.neg_password)
    browser.find_element(By.ID, AuthPageLocators.login_button).click()
    assert browser.find_element(By.XPATH, AuthPageLocators.error_message).text == Asserts.epic_sadface, 'Text error is not as expected'

    # time.sleep(2)


# Adding product to shopping cart via catalog
def test_add_via_catalog(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, CatalogPageLocators.add_to_cart_button).click()
    assert browser.find_element(By.CLASS_NAME, CatalogPageLocators.cart_counter).text == Asserts.one_item_in_cart, \
        "The product wasn't added to cart"
    # time.sleep(2)


# Removing added product via shopping cart
def test_removing_via_cart(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, CatalogPageLocators.add_to_cart_button).click()
    # time.sleep(2)
    browser.find_element(By.CLASS_NAME, CatalogPageLocators.cart_link_button).click()
    # time.sleep(2)
    browser.find_element(By.ID, CartLocators.remove_from_cart_button).click()
    # time.sleep(2)
    assert not browser.find_elements(By.ID, CatalogPageLocators.item_title_link), "The product wasn't removed"
    # time.sleep(2)


# Adding an item to cart via a product card
def test_add_via_product_card(browser):
    test_auth_positive(browser)
    # time.sleep(2)
    browser.find_element(By.ID, CatalogPageLocators.item_title_link).click()
    # time.sleep(2)
    browser.find_element(By.ID, CardPageLocators.add_to_cart_via_card_button).click()
    # time.sleep(2)
    assert browser.find_element(By.CLASS_NAME, CatalogPageLocators.cart_counter).text == Asserts.one_item_in_cart, \
        "The product wasn't added to cart"
    # time.sleep(2)


# Removing added product via product card
def test_delete_via_product_card(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, CatalogPageLocators.item_image_link).click()
    # time.sleep(2)
    browser.find_element(By.ID, CardPageLocators.add_to_cart_via_card_button).click()
    browser.find_element(By. ID, CardPageLocators.remove_from_cart_via_card_button).click()
    # time.sleep(2)
    assert not browser.find_elements(By.CLASS_NAME, CatalogPageLocators.cart_counter), \
        "The product wasn't removed from the cart"


# Redirecting to the product card after clicking on the product image
def test_redirecting_via_product_image(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, CatalogPageLocators.item_image_link).click()
    assert browser.current_url == Urls.item_url, 'The URL is not as expected'


# Redirecting to the product card after clicking on the product name
def test_redirecting_via_product_title(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, CatalogPageLocators.item_title_link).click()
    assert browser.current_url == Urls.item_url, 'The URL is not as expected'


# Placing an order using correct data / without Faker generator
def test_checkout(browser):
    test_add_via_catalog(browser)
    browser.find_element(By.CLASS_NAME, CatalogPageLocators.cart_link_button).click()
    browser.find_element(By.ID, CartLocators.checkout_button).click()
    browser.find_element(By.ID, CheckoutLocators.first_name_field).send_keys(User.gen_firstname)
    browser.find_element(By.ID, CheckoutLocators.last_name_field).send_keys(User.gen_lastname)
    browser.find_element(By.ID, CheckoutLocators.postal_code_field).send_keys(User.gen_postal_code)
    browser.find_element(By.ID, CheckoutLocators.continue_button).click()
    # time.sleep(2)
    browser.find_element(By.ID, CheckoutLocators.finish_button).click()
    assert browser.current_url == Urls.checkout_complete_url, 'The URL is not as expected'
    # time.sleep(2)


# Checking the function of the filter (A to Z)
def test_sort_by_a_to_z(browser):
    test_auth_positive(browser)
    dropdown = browser.find_element(By.CLASS_NAME, CatalogPageLocators.dropdown_sort)
    select = Select(dropdown)
    select.select_by_value(CatalogPageLocators.sort_a_to_z)
    # time.sleep(2)
    products = browser.find_elements(By.CLASS_NAME, CatalogPageLocators.item_name)
    actual_order = [product.text for product in products]
    sorted_order = sorted(actual_order)
    assert actual_order == sorted_order, 'Products is not sorted as A to Z'
    # time.sleep(2)


# Checking the function of the filter (Z to A)
def test_sort_by_z_to_a(browser):
    test_auth_positive(browser)
    dropdown = browser.find_element(By.CLASS_NAME, CatalogPageLocators.dropdown_sort)
    select = Select(dropdown)
    select.select_by_value(CatalogPageLocators.sort_z_to_a)
    # time.sleep(2)
    products = browser.find_elements(By.CLASS_NAME, CatalogPageLocators.item_name)
    actual_order = [product.text for product in products]
    sorted_order = sorted(actual_order, reverse=True)
    assert actual_order == sorted_order, 'Products is not sorted as Z to A'
    # time.sleep(2)


# Checking the function of the filtering by price (Low to High)
def test_sort_by_low_to_high(browser):
    test_auth_positive(browser)
    dropdown = browser.find_element(By.CLASS_NAME, CatalogPageLocators.dropdown_sort)
    select = Select(dropdown)
    select.select_by_value(CatalogPageLocators.sort_low_to_high)
    products = browser.find_elements(By.CLASS_NAME, CatalogPageLocators.item_price)
    actual_order = [float(product.text[1:]) for product in products]
    sorted_order = sorted(actual_order)
    # print(sorted_order)
    assert actual_order == sorted_order, 'Products is not sorted by price by low to high'
    # time.sleep(2)


# Checking the function of the filtering py price (High to Low)
def test_sort_by_high_to_low(browser):
    test_auth_positive(browser)
    dropdown = browser.find_element(By.CLASS_NAME, CatalogPageLocators.dropdown_sort)
    select = Select(dropdown)
    select.select_by_value(CatalogPageLocators.sort_high_to_low)
    products = browser.find_elements(By.CLASS_NAME, CatalogPageLocators.item_price)
    actual_order = [float(product.text[1:]) for product in products]
    sorted_order = sorted(actual_order, reverse=True)
    assert actual_order == sorted_order, 'Products is not sorted by price by high to low'
    # time.sleep(2)


# Checking the functionality of the "About" button
def test_burger(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, BurgerLocators.burger_menu_button).click()
    browser.implicitly_wait(1)
    browser.find_element(By.ID, BurgerLocators.about_button).click()
    # time.sleep(2)
    assert browser.current_url == Urls.about_page_url, 'URL is not as expected'


# Checking the functionality of the "Reset App State
def test_reset_app_state(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, CatalogPageLocators.add_to_cart_button).click()
    browser.find_element(By.ID, BurgerLocators.burger_menu_button).click()
    browser.implicitly_wait(1)
    browser.find_element(By.ID, BurgerLocators.reset_app_button).click()
    assert not browser.find_elements(By.CLASS_NAME, CatalogPageLocators.cart_counter), "An app state wasn't reset"
    # time.sleep(2)


# "Register" button is unable to click if checkbox isn't marked
def test_checkbox_pos(browser):
    browser.get(Urls.base2_url)
    browser.find_element(By.XPATH, RegFormLocators.username_field).send_keys(User.gen_username)
    browser.find_element(By.XPATH, RegFormLocators.password_field).send_keys(User.gen_password)
    assert not browser.find_element(By.XPATH, RegFormLocators.register_button).is_enabled()
    # time.sleep(2)

def test_checkbox_neg(browser):
    browser.get(Urls.base2_url)
    browser.find_element(By.XPATH, RegFormLocators.username_field).send_keys(User.gen_username)
    browser.find_element(By.XPATH, RegFormLocators.password_field).send_keys(User.gen_password)
    browser.find_element(By.XPATH, RegFormLocators.checkbox).click()
    assert browser.find_element(By.XPATH, RegFormLocators.register_button).is_enabled()
    # time.sleep(2)












