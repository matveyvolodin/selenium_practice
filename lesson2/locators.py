class AuthPageLocators:
    username_field = 'user-name'
    password_field = 'password'
    login_button = 'login-button'
    error_message = '//*[@id="login_button_container"]/div/form/div[3]/h3'


class BurgerLocators:
    burger_menu_button = 'react-burger-menu-btn'
    about_button = 'about_sidebar_link'
    reset_app_button = 'reset_sidebar_link'


class CatalogPageLocators:
    add_to_cart_button = 'add-to-cart-sauce-labs-backpack'
    cart_counter = 'shopping_cart_badge'
    cart_link_button = 'shopping_cart_link'
    item_title_link = 'item_4_title_link'
    item_image_link = 'item_4_img_link'
    dropdown_sort = 'product_sort_container'
    item_name = 'inventory_item_name'
    item_price = 'inventory_item_price'
    sort_a_to_z = 'az'
    sort_z_to_a = 'za'
    sort_low_to_high = 'lohi'
    sort_high_to_low = 'hilo'


class CartLocators:
    remove_from_cart_button = 'remove-sauce-labs-backpack'
    checkout_button = 'checkout'

class CheckoutLocators:
    first_name_field = 'first-name'
    last_name_field = 'last-name'
    postal_code_field = 'postal-code'
    continue_button = 'continue'
    finish_button = 'finish'


class CardPageLocators:
    add_to_cart_via_card_button = 'add-to-cart'
    remove_from_cart_via_card_button = 'remove'


class RegFormLocators:
    username_field = '//*[@id="username"]'
    password_field = '//*[@id="password"]'
    checkbox = '//*[@id="agreement"]'
    register_button = '//*[@id="registerButton"]'
