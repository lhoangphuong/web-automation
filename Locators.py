from selenium.webdriver.common.by import By

# define locator for web element
class Locators():
    # --- Home Page Locators ---
    SEARCH_TEXTBOX=(By.ID, "twotabsearchtextbox")
    SEARCH_SUBMIT_BUTTON=(By.XPATH,"//div[contains(@class,'nav-search-submit')]/input")

    # --- Search Results Page Locators ---
    SEARCH_RESULT_LINK=(By.XPATH, "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]")