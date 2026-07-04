from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from config.config import BASE_URL


def test_logout(page):
    login = LoginPage(page)
    login.load(BASE_URL)
    login.login("standard_user", "secret_sauce")

    menu = MenuPage(page)
    menu.logout()

    assert "saucedemo" in page.url