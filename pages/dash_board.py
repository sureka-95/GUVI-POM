# import by module to identify the element
# import exception handling use the timeout exception
# import the pages from pom
# import webdrive waits is used to wait  for a specific condition
# import expected condition to mention the condition to wait
# import built in logging module to track the event what is happening

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from pages.base_pages import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# use the oops method by creating class and methods
class DashboardPage(BasePage):

    #define the initalize method to get logger by xpath
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)
        self.profile_icon = (By.XPATH, "//div[@class='avatar-main-div d-flex cursor mock-interview']//div//img[@alt='S']")  # Update this based on actual HTML
        self.logout_button = (By.XPATH, "//div[normalize-space()='Log out']")
        self.login_button_after_logout = (By.XPATH, "//button[@type='submit']")  # Button after logging out
        self.overlay = (By.CLASS_NAME, "MuiBackdrop-root")

# use webdriver wait to dissapper the message box which overlay the page
    def wait_for_overlay_to_disappear(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.overlay)
        )
# define method logout and pass the argument self
    # use try and exception block for the following steps
    def logout(self):
        try: # following step done using by xpath which mentioned in the above class
            self.wait_for_overlay_to_disappear()
            self.logger.info("Clicking on profile icon...")
            self.click(self.profile_icon)
# logger info is used instead of print ()
            self.logger.info("Clicking on logout...")
            self.click(self.logout_button)

            self.logger.info("Logout successful.")
            # Log or print the exception if something goes wrong during logout
        except TimeoutException as e:
            self.logger.error(f"Timeout while trying to logout: {e}")
            raise # print other than timeout exception if any
        except Exception as e:
            self.logger.error(f"Unexpected error during logout: {e}")
            raise

# is logged out method is create to check the  assert value of logout
    def is_logged_out(self):
        """Return True if the login button is visible again, meaning logout was successful."""
        try:
            return self.is_visible(self.login_button_after_logout)
        except Exception as e:
            self.logger.warning(f"Could not verify logout: {e}")
            return False

    def is_profile_icon_displayed(self):
        try:
            return self.driver.find_element(*self.profile_icon).is_displayed()
        except:
            return False
