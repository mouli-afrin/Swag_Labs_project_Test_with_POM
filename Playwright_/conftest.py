import os
import time
from idlelib import browser

import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

def create_screenshot_folder():
    os.makedirs("Screenshots", exist_ok=True)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        page = item.funcargs.get("page", None)
        if page:
            try:
                create_screenshot_folder()
                timestamp = int(time.time())
                file_path = f"Screenshots/{item.name}_{timestamp}.png"
                # page.wait_for_timeout(1000)
                page.screenshot(path=file_path)
                print(f"❌ Screenshot saved at: {file_path}")
            except Exception as e:
                print(f"⚠️ Could not take screenshot: {e}")
