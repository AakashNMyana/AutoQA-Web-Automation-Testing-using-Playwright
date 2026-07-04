class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.products = ".inventory_item"
        self.prices = ".inventory_item_price"
        self.sort_dropdown = ".product_sort_container"
        self.add_to_cart = "button[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart = ".shopping_cart_link"

    def get_product_count(self):
        return self.page.locator(self.products).count()

    def get_all_prices(self):
        price_elements = self.page.locator(self.prices).all_inner_texts()
        return [float(p.replace("$", "")) for p in price_elements]

    def sort_products(self, option):
        self.page.select_option(self.sort_dropdown, option)

    def add_item(self):
        self.page.click(self.add_to_cart)

    def go_to_cart(self):
        self.page.click(self.cart)