class CartPage:
    def __init__(self, page):
        self.page = page
        self.items = ".cart_item"
        self.item_prices = ".inventory_item_price"

    def get_cart_count(self):
        return self.page.locator(self.items).count()

    def get_item_prices(self):
        prices = self.page.locator(self.item_prices).all_inner_texts()
        return [float(p.replace("$", "")) for p in prices]