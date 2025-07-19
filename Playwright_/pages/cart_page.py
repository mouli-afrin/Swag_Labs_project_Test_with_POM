from config import settings
from config.logger import get_logger

class CartPage:
    def __init__(self, page):
        self.page = page
        self.logger = get_logger("CartPage")

    def add_product_to_cart(self):
        self.logger.info("Adding product to cart")
        self.page.locator(settings.ADD_TO_CART_BTN).click()

    def get_cart_badge_count(self):
        self.logger.info("Checking cart icon for item count")
        return self.page.locator(settings.CART_ICON_BADGE).inner_text()

    def navigate_to_cart(self):
        self.logger.info("Navigating to cart page")
        self.page.locator(settings.CART_ICON).click()

    def get_cart_item_name(self):
        self.logger.info("Fetching product name from cart")
        return self.page.locator(settings.CART_ITEM_NAME).inner_text()
