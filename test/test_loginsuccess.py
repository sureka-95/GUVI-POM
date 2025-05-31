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
def test_login_success(browser):
    # Open Zen portal login page
    browser.get("https://v2.zenclass.in/login")

    # Initialize LoginPage object
    login_page = LoginPage(browser)

    # Provide valid credentials
    valid_email = "surekavj@gmail.com"
    valid_password = "Sureka95"

    # Perform login
    login_page.login(valid_email, valid_password)

    time.sleep(3)

    # Initialize DashboardPage object
    dashboard_page = DashboardPage(browser)

    # Logout (to verify login was successful)
    dashboard_page.logout()

    # Assert logout success (which means login worked)
    assert dashboard_page.is_logged_out(), "Login was not successful or logout failed"
