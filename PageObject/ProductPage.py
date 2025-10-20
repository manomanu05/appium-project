from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        # Locator for the product to click
        self.product_item = (AppiumBy.XPATH, '//android.widget.TextView[@content-desc="test-Item title" and @text="Sauce Labs Backpack"]')
        # Locator for verifying product name on details page
        self.product_name = (AppiumBy.XPATH, '//android.widget.TextView[@text="Sauce Labs Backpack"]')

    # Click product to open details
    def open_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.product_item)
        ).click()

    # Verify product name
    def verify_product_name(self):
        product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.product_name)
        )
        return product.text
