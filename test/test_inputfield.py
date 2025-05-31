# import pytest to create and run the test cases
# import loginpage from pages of pom
# import time module to handle wait
import pytest
from pages.login import LoginPage
import time


# use the fixtures from pytest.ini file
# @pytest.mark.smoke is  a custom marker to categorize test cases
# smoke test which usallu check the high priority tests

@pytest.mark.smoke

# define input field methods and pass the browser argument
# get the browser site
# get login page of browser
def test_username_password_fields_accept_input(browser):
    browser.get("https://v2.zenclass.in/login")
    login_page = LoginPage(browser)

# use the assert statement to check the condition is true or not
    # is displayes method is used to check the web element is visible or not

    # Email field checks
    email_element = browser.find_element(*login_page.email_input)
    assert email_element.is_displayed(), "Email field is not visible"
    assert email_element.is_enabled(), "Email field is not enabled"
    email_element.clear()
    email_element.send_keys("surekavj@gmail.com")
    assert email_element.get_attribute("value") == "surekavj@gmail.com", "Email field did not accept input"

    # Password field checks
    password_element = browser.find_element(*login_page.password_input)
    assert password_element.is_displayed(), "Password field is not visible"
    assert password_element.is_enabled(), "Password field is not enabled"
    password_element.clear()
    password_element.send_keys("Sureka95")
    assert password_element.get_attribute("value") == "Sureka95", "Password field did not accept input"

# negative test case for input fields
# define method for it  and pass the  browser argument
# get the browser
#get the login page of browser
def test_submit_without_input_shows_error(browser):
    browser.get("https://v2.zenclass.in/login")
    login_page = LoginPage(browser)

    # Submit without entering anything
    login_page.click(login_page.login_button)

    # Try detecting error messages (depends on app behavior)
    # use assert statement and check the output is true if it is wrong raise the  command
    error_present = login_page.is_login_error_displayed()
    assert error_present, "Validation error message not shown when input is missing"

# negative test case for input fields
# define method for it  and pass the  browser argument
# get the browser
#get the login page of browser
def test_submit_button_blank_input(browser):
    browser.get("https://v2.zenclass.in/login")
    login_page = LoginPage(browser)

    # Don't enter anything, just click login
    login_page.click(login_page.login_button)
    time.sleep(1)

    # use assert statement and check the output is true if it is wrong raise the command
    assert login_page.is_login_error_displayed(), "No error shown on submitting empty credentials"
