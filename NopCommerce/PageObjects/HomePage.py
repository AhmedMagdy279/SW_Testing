import time
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
        self.featuredProducts_add_to_cart_btns = (By.XPATH, "//button[@class='button-2 product-box-add-to-cart-button']")
        self.notification_bar_close_btn = (By.XPATH, "//span[@class='close']")
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

    def click_add_to_cart_featured_product_htc_one_m8(self):
        htc_featured = self.driver.find_elements(*self.featuredProducts_add_to_cart_btns)
        htc_featured[2].click()

    def close_notification_bar(self):
        time.sleep(1)
        self.driver.find_element(*self.notification_bar_close_btn).click()

    def scroll_page(self, x_axis, y_axis):
        self.action.scroll_by_amount(x_axis, y_axis).perform()
