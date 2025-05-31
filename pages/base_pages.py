# import built in logging module to track the event what is happening
# used instead of print(?)
import logging

# import webdrive wait to reach expected condition
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# create base page class
#  define different methods
class BasePage:
    def __init__(self, driver):# constructor method used to initialize new object
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logging.getLogger(__name__)

    def click(self, locator):
        try: # try block used to attempt the following steps for login process
            self.logger.info(f"Clicking on element: {locator}")
            self.wait.until(EC.element_to_be_clickable(locator)).click()

            # Log or print the exception if something goes wrong during login
        except Exception as e:
            self.logger.error(f"Failed to click {locator}: {e}")
            raise
# create enter text method to locate and type text by self
    def enter_text(self, locator, text):
        try: # try block used to attempt the following steps for login process
            self.logger.info(f"Entering text into: {locator}")
            self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
        except Exception as e:
            self.logger.error(f"Failed to enter text in {locator}: {e}")
            raise

# is visible method use the parameter of self and locator
    def is_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except Exception:
            return False
