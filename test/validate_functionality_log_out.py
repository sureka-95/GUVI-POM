# import pytest to create and run the test cases
# import loginpage from pages of pom
#import dashboard page from pages directory of pom
# import time module to handle wait
import pytest
from pages.login import LoginPage
from pages.dash_board  import DashboardPage
import time

# use the fixtures from pytest.ini file
# @pytest.mark.smoke is  a custom marker to categorize test cases
# smoke test which usallu check the high priority tests

@pytest.mark.smoke

# define method for test cases
# tests the logout button function is working properly

def test_logout_button_functionality(browser):
    # get the website from the browser
    browser.get("https://v2.zenclass.in/login")
# use the class of loginpage and dashboard browsers
    login_page = LoginPage(browser)
    dashboard_page = DashboardPage(browser)

    # Login with valid credentials
    login_page.login("valid@gmail.com", "password")
    time.sleep(3)

    # Logout
    dashboard_page.logout()
    time.sleep(2)

    # Assert that user is redirected back to login page
    assert dashboard_page.is_logged_out(), "Logout failed or user not redirected to login page"
