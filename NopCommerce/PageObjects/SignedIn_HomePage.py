from selenium.webdriver.common.by import By


class SignedInHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.my_account = (By.XPATH, "//a[@class='ico-account']")
        self.log_out = (By.XPATH, "//a[@class='ico-logout']")
        self.shopping_cart = (By.XPATH, "//span[@class='cart-label']")

    def click_my_account(self):
        self.driver.find_element(self.my_account).click()

    def click_logout(self):
        self.driver.find_element(self.log_out).click()

    def click_shopping_cart(self):
        self.driver.find_element(self.shopping_cart).click()
