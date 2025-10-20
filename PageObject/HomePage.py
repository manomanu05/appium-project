from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.menu_button = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Menu"]/android.view.ViewGroup/android.widget.ImageView')
        self.logout_button = (AppiumBy.XPATH, '//android.widget.TextView[@text="LOGOUT"]')

    # Open menu
    def open_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_button)
        ).click()

    # Click logout
    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_button)
        ).click()

    # Combined logout action
    def logout(self):
        self.open_menu()
        self.click_logout()
