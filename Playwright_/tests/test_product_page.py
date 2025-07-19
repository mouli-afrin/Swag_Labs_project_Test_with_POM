from pages.Login_page import LoginPage
from pages.product_page import ProductPage
from config import settings
from config.logger import get_logger
import time

logger = get_logger("ProductPageTest")


def test_product_page_items(page):
    logger.info("TC_003: Product page validation started")

    # Step 1: Login
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    # Step 2: Verify product page
    product_page = ProductPage(page)

    assert product_page.is_expected_product_count(settings.EXPECTED_PRODUCT_COUNT), (
        f"❌ Expected {settings.EXPECTED_PRODUCT_COUNT} products, but got {len(product_page.get_product_titles())}"
    )

    assert product_page.is_specific_product_visible(settings.EXPECTED_PRODUCT), (
        f"❌ Product '{settings.EXPECTED_PRODUCT}' not found in product list"
    )

    logger.info("✅ TC_003: Product page test passed successfully")


def test_specific_product_visible(page):
    logger.info("TC_004: Specific product title validation started")

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    product_page = ProductPage(page)
    expected_name = settings.EXPECTED_PRODUCT

    assert product_page.is_specific_product_visible(expected_name), (
        f"❌ Product '{expected_name}' not found in product list"
    )

    logger.info("✅ TC_004: Specific product title validation passed")
    
