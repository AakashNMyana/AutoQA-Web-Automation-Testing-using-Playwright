class MenuPage:
    def __init__(self, page):
        self.page = page
        self.menu_btn = "#react-burger-menu-btn"
        self.logout_btn = "#logout_sidebar_link"

    def logout(self):
        self.page.click(self.menu_btn)
        self.page.click(self.logout_btn)
