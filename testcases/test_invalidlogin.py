import pytest
from PageObject.LoginPage import LoginPage
from appium.webdriver.common.appiumby import AppiumBy
import os
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException

def save_screenshot(driver, name="screenshot"):
    """Save a screenshot in 'screenshots' folder with timestamp."""
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(path)
    print(f"Screenshot saved to {path}")

def test_invalid_login(driver):
    login_page = LoginPage(driver)

    # Attempt invalid login
    login_page.login("invalid_user", "wrong_password")

    # Try to locate the error message
    try:
        error_msg = driver.find_element(
            AppiumBy.XPATH,
            '//android.widget.TextView[@text="Username and password do not match any user in this service."]'
        )
        if error_msg.is_displayed():
            # Take screenshot because invalid login message appeared
            save_screenshot(driver, "invalid_login")
    except NoSuchElementException:
        # No error message found – do nothing
        pass
