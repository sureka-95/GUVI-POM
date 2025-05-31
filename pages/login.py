from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from pages.base_pages import BasePage



class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.email_input = (By.ID, ":r0:")
        self.password_input = (By.ID, ":r1:")
        self.login_button = (By.XPATH, "//button[@type='submit']")
        self.error_message = (By.XPATH, "//p[@id=':r1:-helper-text']")

    def login(self, email, password):
        try:
            self.logger.info("Attempting to log in.")
            self.enter_text(self.email_input, email)
            self.enter_text(self.password_input, password)
            self.click(self.login_button)
            self.logger.info("Login submitted.")

        except Exception as e:
            print(f"Error while logging in: {e}")
            raise


    def is_login_error_displayed(self, timeout=5):

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self.error_message)
            )
            return True
        except  (TimeoutException, NoSuchElementException):
            return False
        except Exception as e:
            print(f"Unexpected error checking login error: {e}")
            raise