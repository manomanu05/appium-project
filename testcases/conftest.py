import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utilities.ReadConfig import ReadConfig

@pytest.fixture(scope="function")
def driver():
    desired_caps = {
        'platformName': ReadConfig.get_config('Appium', 'platformName'),
        'platformVersion': ReadConfig.get_config('Appium', 'platformVersion'),
        'deviceName': ReadConfig.get_config('Appium', 'deviceName'),
        'udid': ReadConfig.get_config('Appium', 'udid'),
        'automationName': ReadConfig.get_config('Appium', 'automationName'),
        'appPackage': ReadConfig.get_config('Appium', 'appPackage'),
        'appActivity': ReadConfig.get_config('Appium', 'appActivity'),
        'noReset': ReadConfig.get_bool('Appium', 'noReset')
    }

    options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()