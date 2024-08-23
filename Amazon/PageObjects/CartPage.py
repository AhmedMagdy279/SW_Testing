from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_btn = (By.XPATH, "//input[@value='Proceed to checkout']")
        self.action = ActionChains(self.driver)

    def check_item_in_cart(self, item_name):
        cart_items = self.driver.find_elements(By.XPATH,
                                               "//span[@class='a-truncate-cut' and not(contains(text(), 'in Office "
                                               "Products'))]")
        return [item.text for item in cart_items]

    def scroll_page(self, x_axis, y_axis):
        self.action.scroll_by_amount(x_axis, y_axis).perform()

    def click_and_goto_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()
