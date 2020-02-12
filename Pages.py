# system module
import time

# selenium module
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# project module
from InputData import InputData
from Locators import Locators

##########################################################
#                                                        #
#       Where the Page Object Model happen!              #
#                                                        #
##########################################################
   
class BaseClass():
    ''' This class is the parent class for all other pages. '''
    ''' It contain common functions, can be used by all pages.'''

    # this method is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver = driver

    # this method perform click function
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    # this method perform text input function
    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10). until(EC.visibility_of_element_located(locator)).send_keys(text)

    # this method perform assert text in element function
    def assert_element_text(self, locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        assert web_element.text == element_text

##############################################################################################################################

# --- Start Writing code for Pages ---

class HomePage(BaseClass):
    ''' Home Page of Amazon.com '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(InputData.BASE_URL)
        
    def search(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        self.enter_text(Locators.SEARCH_TEXTBOX, InputData.SEARCH_TERM)
        self.click(Locators.SEARCH_SUBMIT_BUTTON)