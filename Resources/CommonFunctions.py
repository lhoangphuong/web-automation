# system module
import time

# selenium module
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# project module
from Resources.Input import Input
from Resources.Locators import Locators

class BaseClass():
    ''' This class is the parent class for all other pages. '''
    ''' It contain common functions, can be used by all pages.'''

    # this method is called upon creation of a new object of this BaseClass
    def __init__(self, driver):
        self.driver = driver
        

    # --- Method for all common functions ---

    # click function
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    # input text function
    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10). until(EC.visibility_of_element_located(locator)).send_keys(text)

    # assert text in elements
    def assert_element_text(self, locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        assert web_element.text == element_text
