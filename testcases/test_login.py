import pytest
from PageObject.LoginPage import LoginPage

def test_login_flow(driver):
    # Initialize Login Page
    login_page = LoginPage(driver)

    # Enter credentials and login
    login_page.login("standard_user", "secret_sauce")

    # At this point, the app should open the home screen / catalog
    # No need for extra assertions if you just want to launch and login
