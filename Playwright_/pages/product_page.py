from config import settings
from config.logger import get_logger

class ProductPage:
    def __init__(self, page):
        self.page = page
        self.logger = get_logger("ProductPage")

    def get_product_titles(self):
        self.logger.info("Fetching all product titles from inventory page")
        return self.page.locator(settings.PRODUCT_TITLES).all_inner_texts()

    def is_specific_product_visible(self, expected_name):
        self.logger.info(f"Checking if product '{expected_name}' is listed")
        product_names = self.get_product_titles()
        return expected_name in product_names

    def is_expected_product_count(self, expected_count):
        self.logger.info("Validating total number of listed products")
        actual_count = len(self.get_product_titles())
        return actual_count == expected_count
