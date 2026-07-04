from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.api_helper import get_products_count
from config.config import BASE_URL


def test_ui_api_product_validation(page):
    login = LoginPage(page)
    login.load(BASE_URL)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    ui_count = inventory.get_product_count()
    api_count = get_products_count()

    assert ui_count <= api_count