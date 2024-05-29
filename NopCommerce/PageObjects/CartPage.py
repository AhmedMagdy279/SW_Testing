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
        self.input_terms_of_service = (By.ID, "termsofservice")
        self.checkout_btn = (By.ID, "checkout")
        self.action = ActionChains(self.driver)

    def scroll_page(self, x_axis, y_axis):
        self.action.scroll_by_amount(x_axis, y_axis).perform()

    def get_HTC_one_M8_quantity(self):
        return self.driver.find_element(*self.input_quantity_HTC_one_M8).get_attribute("value")

    def remove_HTC_one_M8_from_cart(self):
        self.driver.find_element(*self.remove_btn_HTC_one_M8).click()

    def click_terms_of_service(self):
        self.driver.find_element(*self.input_terms_of_service).click()

    def click_and_goto_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()
