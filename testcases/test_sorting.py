import pytest
from PageObject.LoginPage import LoginPage
from PageObject.SortingPage import SortingPage

def test_login_and_apply_filter(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    #Open filter modal
    sorting_page = SortingPage(driver)
    sorting_page.open_filter_modal()

    # Select "Price (low to high)"
    sorting_page.select_price_low_to_high()
