from config import settings
from config.logger import get_logger
class LoginPage:



    def __init__(self, page):
        self.page = page
        self.logger = get_logger("LoginPage")

    def goto(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.logger.info("Filling username and password and logging in")
        self.page.locator(settings.USERNAME_INPUT).fill(username)
        self.page.locator(settings.PASSWORD_INPUT).fill(password)
        self.page.locator(settings.LOGIN_BUTTON).click()

    def is_login_successful(self):
        self.logger.info("Checking if login is successful")
        return self.page.locator(settings.PRODUCT_HEADER).inner_text()

    def is_login_failed(self):
        self.logger.info("Checking if login is failed")
        return self.page.locator(settings.PRODUCT_HEADER).inner_text()

    def get_error_message(self):
        self.logger.info("Getting error message")
        # Wait and return error message if login fails
        self.page.wait_for_selector(settings.ERROR_MESSAGE, timeout=5000)
        return self.page.locator(settings.ERROR_MESSAGE).inner_text()