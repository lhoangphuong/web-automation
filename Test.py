# system module
import time

# unittest for test framework
# HtmlTestRunner for report
import unittest
import HtmlTestRunner

# selenium module
from selenium import webdriver

# project module
from InputData import InputData
from Locators import Locators
from Pages import HomePage

##########################################################
#                                                        #
#       Perform our test with unittest framework         #
#                                                        #
##########################################################

class Test_Base(unittest.TestCase):
    def setUp(self):
        # Setting up how we want Chrome to run
        self.driver=webdriver.Chrome(InputData.CHROME_DRIVER)
        #browser should be loaded in maximized window
        self.driver.maximize_window()

    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()

class Test_AMZ_Search(Test_Base):
    def setUp(self):
        super().setUp()

    def test_home_page(self):
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.homePage=HomePage(self.driver)
        # assert if the title of Home Page contains Amazon.in
        self.assertIn(InputData.HOME_PAGE_TITLE, self.homePage.driver.title)
        self.homePage.search()
        time.sleep(5)

# Boiler plate code to get the code running
if __name__ == '__main__':
    # specify path where the HTML reports for testcase execution are to be generated
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/web-automation/Reports'))


