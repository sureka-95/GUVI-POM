# import pytest to create and run the test cases
# import loginpage from pages of pom
# import time module to handle wait

import pytest
from pages.login import LoginPage
import time

# use the fixtures from pytest.ini file
# @pytest.mark.smoke is  a custom marker to categorize test cases
# smoke test which usallu check the high priority tests
# negative is indicate the test case type

@pytest.mark.negative

# define the method for test the login unsuccessfull and pass the argument browser
def test_login_unsuccessful(browser):
    # get the browser
    browser.get("https://v2.zenclass.in/login")
# use the class of browser from login page
    login_page = LoginPage(browser)

# use the invalid user id and password value and pass with their attributes
    invalid_email = "invaliduser@example.com"
    invalid_password = "wrongpassword"

    login_page.login(invalid_email, invalid_password)

    time.sleep(3)
    # Wait or directly check error message visible
    # to check the outcome uses the assert statement to verify the condition is true or not
    assert login_page.is_login_error_displayed(), "Expected login error message not displayed"
