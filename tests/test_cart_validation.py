from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from config.config import BASE_URL


def test_cart_price_validation(page):
    login = LoginPage(page)
    login.load(BASE_URL)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.add_item()
    inventory.go_to_cart()

    cart = CartPage(page)
    prices = cart.get_item_prices()

    assert sum(prices) > 0