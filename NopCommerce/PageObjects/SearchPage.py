from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.log_in = (By.XPATH, "//a[@class='ico-login']")
        self.register = (By.XPATH, "//a[@class='ico-register']")
        self.shopping_cart = (By.XPATH, "//span[@class='cart-label']")
        self.search_textbox = (By.ID, "small-searchterms")
        self.search_button = (By.XPATH, "//button[text()='Search']")
        self.add_product_to_cart = (By.XPATH, "//button[text()='Add to cart']")
        self.notification_bar = (By.CSS_SELECTOR, "[class*='bar-notification']")
        self.action = ActionChains(self.driver)

    def scroll_page(self, x_axis, y_axis):
        self.action.scroll_by_amount(x_axis, y_axis).perform()

    def click_on_first_item_add_to_cart(self):
        self.driver.find_element(*self.add_product_to_cart).click()

    def get_notification_bar(self):
        return self.driver.find_element(*self.notification_bar)

