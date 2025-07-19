from pages.Login_page import LoginPage
from pages.cart_page import CartPage
from config import settings
from config.logger import get_logger
import time

logger = get_logger("CartTest")

def test_add_product_shows_cart_badge(page):
    logger.info("TC_005: Add product and verify cart badge started")

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    cart_page = CartPage(page)
    cart_page.add_product_to_cart()

    badge_count = cart_page.get_cart_badge_count()
    assert badge_count == "1", f"❌ Expected cart badge '1', but got '{badge_count}'"

    logger.info("✅ TC_005: Cart badge reflects added product")


def test_cart_contains_added_product(page):
    logger.info("TC_006: Verify correct item is in cart started")

    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    cart_page = CartPage(page)
    cart_page.add_product_to_cart()
    cart_page.navigate_to_cart()

    product_name = cart_page.get_cart_item_name()
    assert product_name == settings.EXPECTED_PRODUCT, f"❌ Expected product '{settings.EXPECTED_PRODUCT}', but got '{product_name}'"

    logger.info("✅ TC_006: Cart displays correct product")
