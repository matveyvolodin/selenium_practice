from faker import Faker

faker_en = Faker('en')
Faker.seed()


class User:
    pos_username = 'standard_user'
    pos_password = 'secret_sauce'
    neg_username = 'user'
    neg_password = 'user'
    gen_firstname = faker_en.first_name()
    gen_lastname = faker_en.last_name()
    gen_postal_code = faker_en.postalcode()
    gen_username = faker_en.user_name()
    gen_password = faker_en.password()


class Urls:
    base_url = 'https://www.saucedemo.com/'
    catalog_url = 'https://www.saucedemo.com/inventory.html'
    item_url = 'https://www.saucedemo.com/inventory-item.html?id=4'
    checkout_complete_url = 'https://www.saucedemo.com/checkout-complete.html'
    about_page_url = 'https://saucelabs.com/'
    base2_url = 'https://victoretc.github.io/webelements_information/'



class Asserts:
    epic_sadface = 'Epic sadface: Username and password do not match any user in this service'
    one_item_in_cart = '1'


# assert_messages

