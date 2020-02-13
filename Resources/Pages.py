# project module
from Resources.Input import Input
from Resources.Locators import Locators
from Resources.CommonFunctions import BaseClass

##########################################################
#                                                        #
#       Where the Page Object Model happen!              #
#                                                        #
##########################################################

class HomePage(BaseClass):
    ''' Home Page of Amazon.com '''
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(Input.BASE_URL)
        
    def search(self):
        self.driver.find_element(*Locators.SEARCH_TEXTBOX).clear()
        self.enter_text(Locators.SEARCH_TEXTBOX, Input.SEARCH_TERM)
        self.click(Locators.SEARCH_SUBMIT_BUTTON)

class SearchResultPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def click_search_result(self):
        self.click(Locators.SEARCH_RESULT_LINK)

class CartPage(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def click_add_to_cart(self):
        self.click(Locators.ADD_TO_CART_BUTTON)