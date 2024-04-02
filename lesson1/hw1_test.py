import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select


# Homework for lesson 1
# Need to write autotests for saucedemo website: "https://www.saucedemo.com/" to cover next functionalities:

url = 'https://www.saucedemo.com/'


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# Authorisation using correct data (standard_user, secret_sauce)
def test_auth_positive(browser):
    user_name = 'standard_user'
    password = 'secret_sauce'
    browser.get(url)
    browser.find_element(By.ID, 'user-name').send_keys(user_name)
    browser.find_element(By.ID, 'password').send_keys(password)
    browser.find_element(By.ID, 'login-button').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', 'url does not match'
    # time.sleep(2)


# Authorisation using incorrect data (user, user)
def test_auth_negative(browser):
    user_name = 'user'
    password = 'user'
    browser.get(url)
    browser.find_element(By.ID, 'user-name').send_keys(user_name)
    browser.find_element(By.ID, 'password').send_keys(password)
    browser.find_element(By.ID, 'login-button').click()
    assert (browser.find_element(By.XPATH, '//div[3]/h3').text ==
            'Epic sadface: Username and password do not match any user in this service'),\
        'The error text does not correspond to the expected value'
    # time.sleep(2)


# Adding product to shopping cart via catalog
def test_add_via_catalog(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    assert browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1', \
        "The product wasn't added to cart"
    # time.sleep(2)


# Removing added product via shopping cart
def test_removing_via_cart(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    # time.sleep(2)
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    # time.sleep(2)
    browser.find_element(By.ID, 'remove-sauce-labs-backpack').click()
    # time.sleep(2)
    assert not browser.find_elements(By.ID, 'item_4_title_link'), "The product wasn't removed"
    # time.sleep(2)


# Adding an item to cart via a product card
def test_add_via_product_card(browser):
    test_auth_positive(browser)
    # time.sleep(2)
    browser.find_element(By.ID, 'item_4_title_link').click()
    # time.sleep(2)
    browser.find_element(By.ID, 'add-to-cart').click()
    time.sleep(2)
    assert browser.find_element(By.CLASS_NAME, 'shopping_cart_badge').text == '1', \
        "The product wasn't added to cart"
    # time.sleep(2)


# Removing added product via shopping cart
def test_delete_via_product_card(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, 'item_4_img_link').click()
    browser.find_element(By.ID, 'add-to-cart').click()
    browser.find_element(By. ID, 'remove').click()
    time.sleep(2)
    assert not browser.find_elements(By.CLASS_NAME, 'shopping_cart_badge'),\
        "The product wasn't removed from the cart"


# Redirecting to the product card after clicking on the product image
def test_redirecting_via_product_image(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, 'item_4_img_link').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', 'The URL is not as expected'


# Redirecting to the product card after clicking on the product name
def test_redirecting_via_product_title(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, 'item_4_title_link').click()
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', 'The URL is not as expected'


# Placing an order using correct data / without Faker generator
def test_checkout(browser):
    test_add_via_catalog(browser)
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    browser.find_element(By.ID, 'checkout').click()
    browser.find_element(By.ID, 'first-name').send_keys('Thomas')
    browser.find_element(By.ID, 'last-name').send_keys('Jefferson')
    browser.find_element(By.ID, 'postal-code').send_keys('3331G33')
    browser.find_element(By.ID, 'continue').click()
    # time.sleep(2)
    browser.find_element(By.ID, 'finish').click()
    assert browser.current_url == 'https://www.saucedemo.com/checkout-complete.html', 'The URL is not as expected'
    time.sleep(2)


# Checking the function of the filter (A to Z)
def test_sort_by_a_to_z(browser):
    test_auth_positive(browser)
    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    select = Select(dropdown)
    select.select_by_value('az')
    # time.sleep(2)
    products = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    actual_order = [product.text for product in products]
    sorted_order = sorted(actual_order)
    assert actual_order == sorted_order, 'Products is not sorted as A to Z'
    # time.sleep(2)


# Checking the function of the filter (Z to A)
def test_sort_by_z_to_a(browser):
    test_auth_positive(browser)
    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    select = Select(dropdown)
    select.select_by_value('za')
    # time.sleep(2)
    products = browser.find_elements(By.CLASS_NAME, 'inventory_item_name')
    actual_order = [product.text for product in products]
    sorted_order = sorted(actual_order, reverse=True)
    assert  actual_order == sorted_order, 'Products is not sorted as Z to A'
    # time.sleep(2)


# Checking the function of the filter (Low to High)
def test_sort_by_low_to_high(browser):
    test_auth_positive(browser)
    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    select = Select(dropdown)
    select.select_by_value('lohi')
    products = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    actual_order = [float(product.text[1:]) for product in products]
    sorted_order = sorted(actual_order)
    # print(sorted_order)
    assert actual_order == sorted_order, 'Products is not sorted by price from low to high'
    time.sleep(2)

# Checking the function of the filter (Low to High)
def test_sort_by_high_to_low(browser):
    test_auth_positive(browser)
    dropdown = browser.find_element(By.CLASS_NAME, 'product_sort_container')
    select = Select(dropdown)
    select.select_by_value('hilo')
    products = browser.find_elements(By.CLASS_NAME, 'inventory_item_price')
    actual_order = [float(product.text[1:]) for product in products]
    sorted_order = sorted(actual_order, reverse=True)
    assert actual_order == sorted_order, 'Products is not sorted by price from low to high'
    time.sleep(2)


# Checking the functionality of the "About" button
def test_burger(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    browser.implicitly_wait(1)
    browser.find_element(By.ID, 'about_sidebar_link').click()
    time.sleep(2)
    assert browser.current_url == 'https://saucelabs.com/', 'URL is not as expected'


# Checking the functionality of the "Reset App State
def test_reset_app_state(browser):
    test_auth_positive(browser)
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    browser.find_element(By.ID, 'react-burger-menu-btn').click()
    browser.implicitly_wait(1)
    browser.find_element(By.ID, 'reset_sidebar_link').click()
    assert not browser.find_elements(By.CLASS_NAME, 'shopping_cart_badge'), "App State wasn't reset"
    time.sleep(2)













