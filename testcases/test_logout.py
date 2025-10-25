import pytest
from PageObject.LoginPage import LoginPage
from PageObject.HomePage import HomePage

def test_login_and_logout(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Perform logout
    home_page = HomePage(driver)
    home_page.logout()

    
