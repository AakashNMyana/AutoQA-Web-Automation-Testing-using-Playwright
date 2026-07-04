from pages.login_page import LoginPage
from config.config import BASE_URL


def test_login(page):
    login = LoginPage(page)
    login.load(BASE_URL)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in page.url