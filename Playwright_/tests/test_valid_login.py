from pages.Login_page import LoginPage
from config.logger import get_logger
import time
logger = get_logger("TestLogin")
def test_login_success(page):
    logger.info("TC_001:  test_valid_login started")
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful()
    logger.info("  test_valid_login ended")

def test_login_failed(page):
    logger.info("TC002: test_login_failed_started")
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("wrong_user", "wrong_pass")

    expected_error = "Epic sadface: Username and password do not match any user in this service"
    actual_error = login_page.get_error_message()

    assert actual_error == actual_error
    logger.info("  test_login_failed_ended")
