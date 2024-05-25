from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.log_in = (By.XPATH, "//a[@class='ico-login']")
        self.register = (By.XPATH, "//a[@class='ico-register']")
        self.shopping_cart = (By.XPATH, "//span[@class='cart-label']")
        self.search_textbox = (By.ID, "small-searchterms")
        self.search_button = (By.XPATH, "//button[text()='Search']")
        self.action = ActionChains(self.driver)

    def click_login(self):
        self.driver.find_element(*self.log_in).click()

    def click_register(self):
        self.driver.find_element(*self.register).click()

    def click_shopping_cart(self):
        self.driver.find_element(*self.shopping_cart).click()

    def enter_search_text(self, search_item):
        self.driver.find_element(*self.search_textbox).send_keys(search_item)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

