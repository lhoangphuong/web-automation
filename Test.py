#########################
#  Pre install package  #
#########################

##################################################################################

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == '__main__':
    install('selenium')
    install('html-testRunner')

##################################################################################    


# system module
import time

# unittest for test framework
# HtmlTestRunner for report
import unittest
import HtmlTestRunner

# selenium module
from selenium import webdriver

# project module
from Resources.Input import Input
from Resources.Locators import Locators
from Resources.Pages import HomePage, SearchResultPage

##########################################################
#                                                        #
#       Perform our test with unittest framework         #
#                                                        #
##########################################################

class Test_Base(unittest.TestCase):
    def setUp(self):
        # Setting up how we want Chrome to run
        self.driver=webdriver.Chrome(Input.CHROME_DRIVER)
        #browser should be loaded in maximized window
        self.driver.maximize_window()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()

class Test_AMZ_Search(Test_Base):
    def setUp(self):
        super().setUp()

    def test_home_page_load_successfully(self):
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.homePage=HomePage(self.driver)
        # assert if the title of Home Page contains Amazon.in
        self.assertIn(Input.HOME_PAGE_TITLE, self.homePage.driver.title)
        time.sleep(5)

    def test_user_should_be_able_search(self):
        self.homePage = HomePage(self.driver)
        self.searchResultPage = SearchResultPage(self.driver)
        self.homePage.search()
        self.searchResultPage.click_search_result()
        time.sleep(5)
        
# Boiler plate code to get the code running
if __name__ == '__main__':
    # specify path where the HTML reports for testcase execution are to be generated
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/web-automation/Reports'))


