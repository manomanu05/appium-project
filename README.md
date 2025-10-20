Appium Automation Project Report
Project Overview
This project automates testing for the Swag Labs Mobile App (Android) using Appium with Python and Pytest. It includes automation for login, logout, product catalog, cart, and sorting functionalities. Screenshots are captured for failed login attempts and after applying sorting filters.
________________________________________
Project Structure
appium-project
│
├─ .venv                       # Virtual environment
├─ Configurations
│  ├─ __init__.py
│  └─ config.ini               # Configuration file for driver and environment settings
├─ PageObject                  # Page Object Model classes
│  ├─ __init__.py
│  ├─ CatalogPage.py
│  ├─ HomePage.py
│  ├─ LoginPage.py
│  ├─ ProductPage.py
│  └─ SortingPage.py
├─ screenshots                 # Folder storing screenshots
│  ├─ invalid_login_20251020_233817.png
│  └─ price_low_to_high.png
├─ testcases                   # Test cases written using Pytest
│  ├─ __init__.py
│  ├─ conftest.py
│  ├─ test_invalidlogin.py
│  ├─ test_login.py
│  ├─ test_logout.py
│  ├─ test_product.py
│  ├─ test_product_cart.py
│  └─ test_sorting.py
└─ utilities                   # Utility classes
   ├─ __init__.py
   └─ ReadConfig.py
________________________________________
Test Scenarios Automated
1.	Login Tests
o	Valid login
o	Invalid login (with screenshot capture)
o	Empty username
o	Empty password
2.	Logout Test
o	Logout after successful login
3.	Product Catalog & Cart
o	Verify product names
o	Add products to cart
o	Verify cart content
4.	Sorting
o	Apply Price (low to high) filter
o	Verify sorted products
o	Take screenshot after sorting
________________________________________
Appium Desired Capabilities
{
  "platformName": "Android",
  "appium:platformVersion": "10",
  "appium:deviceName": "vivo_device",
  "appium:udid": "9XWOYTMRZXHE8HT4",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.swaglabsmobileapp",
  "appium:appActivity": "com.swaglabsmobileapp.SplashActivity",
  "appium:noReset": true
}
________________________________________
Tools & Software Used
Tool / Library	Version / Details
Appium Server	2.x
Appium Python Client	4.0.0
Python	3.10+
Pytest	8.1.1
Pytest-html	4.0.2
Allure-Pytest	2.13.5
Selenium	4.x
UiAutomator2	Default Appium Android Automation Engine
Android Device	Vivo, Android 10, UDID: 9XWOYTMRZXHE8HT4
IDE	  PyCharm
________________________________________
Screenshots
•	invalid_login_YYYYMMDD_HHMMSS.png → Captured after invalid login attempt.
•	price_low_to_high.png → Captured after applying the "Price (low to high)" filter.
________________________________________
How to Run Tests
1.	Start Appium server: appium --relaxed-security
2.	Connect the Android device or launch emulator.
3.	Activate virtual environment:
source .venv/bin/activate   # Linux / Mac
.venv\Scripts\activate      # Windows
4.	Run tests using Pytest:
pytest testcases/ --html=reports/report.html
5.	Check screenshots in screenshots/ folder.
________________________________________
Notes
•	Page Object Model (POM) is used for maintainability.
•	Explicit waits (WebDriverWait + expected_conditions) ensure stable automation.
•	All locators are based on accessibility ID or XPath.

