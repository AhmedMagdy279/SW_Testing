import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_textbox = (By.ID, "small-searchterms")
        self.search_button = (By.XPATH, "//button[text()='Search']")
        self.input_quantity_HTC_one_M8 = (By.XPATH, "//td/a[text()='HTC One M8 Android L 5.0 Lollipop']"
                                                    "/../../td[@class='quantity']/div/input")
        self.remove_btn_HTC_one_M8 = (By.XPATH, "//td/a[text()='HTC One M8 Android L 5.0 Lollipop']/../../td["
                                                "@class='remove-from-cart']/button")

    def get_HTC_one_M8_quantity(self):
        return self.driver.find_element(*self.input_quantity_HTC_one_M8).get_attribute("value")

    def remove_HTC_one_M8_from_cart(self):
        self.driver.find_element(*self.remove_btn_HTC_one_M8).click()
