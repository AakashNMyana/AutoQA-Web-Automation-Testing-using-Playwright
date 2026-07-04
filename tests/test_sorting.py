from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import BASE_URL


def test_sort_products(page):
    login = LoginPage(page)
    login.load(BASE_URL)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.sort_products("lohi")
    prices = inventory.get_all_prices()

    assert prices == sorted(prices)