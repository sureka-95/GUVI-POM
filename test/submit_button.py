# import pytest to create and run the test cases
# import loginpage from pages of pom
#import dashboard page from pages directory of pom
# import time module to handle wait
import pytest
from pages.login import LoginPage
from pages.dash_board import DashboardPage
import time

# use the fixtures from pytest.ini file
# @pytest.mark.smoke is  a custom marker to categorize test cases
# smoke test which usallu check the high priority tests

@pytest.mark.smoke
def test_submit_button_works_with_valid_input(browser):
    browser.get("https://v2.zenclass.in/login")
    login_page = LoginPage(browser)

    valid_email = "surekavj@gmail.com"
    valid_password = "Sureka95"

    login_page.login(valid_email, valid_password)
    time.sleep(3)

    # Assuming successful login leads to dashboard where logout button exists
    dashboard_page = DashboardPage(browser)
    assert dashboard_page.is_profile_icon_displayed(), "Login was not successful, dashboard not loaded"


def test_submit_button_with_invalid_input_shows_error(browser):
    browser.get("https://v2.zenclass.in/login")
    login_page = LoginPage(browser)

    invalid_email = "wrong@example.com"
    invalid_password = "invalidpass"

    login_page.login(invalid_email, invalid_password)
    time.sleep(2)

    assert login_page.is_login_error_displayed(), "Error message not shown for invalid login"
