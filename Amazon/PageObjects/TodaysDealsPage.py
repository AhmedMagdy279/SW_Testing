import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, StaleElementReferenceException


class TodaysDealsPage:
    def __init__(self, driver):
        self.filter_item = None
        self.driver = driver
        self.shopping_cart = (By.ID, "nav-cart")
        self.item_added_notification = (By.XPATH, "//strong[text()='Item Added']")
        self.see_more_options = (By.XPATH, "//button/a[text()='See more']")
        self.action = ActionChains(self.driver)

    def expand_more_options(self):
        self.driver.find_element(*self.see_more_options).click()

    def apply_filter_name(self, filter_name):
        element = self.driver.find_element(By.XPATH, f"//span[contains(text(), '{filter_name}')]")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def verify_applied_filter(self, filter_name):
        try:
            element = self.driver.find_element(By.XPATH, f"//button/span[contains(text(), '{filter_name}')]")
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            return True
        except NoSuchElementException:
            return False

    def select_item_index_to_cart(self, item_number):
        all_items = self.driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        all_items[item_number-1].click()
        items_names = self.driver.find_elements(By.XPATH, "//h2/a/span")
        return items_names[item_number-1].text

    def verify_item_added_to_cart(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.item_added_notification)
            )
            return True
        except NoSuchElementException:
            return False

    def go_to_shopping_cart(self):
        self.driver.find_element(*self.shopping_cart).click()
        #time.sleep(2)

    def scroll_page(self, x_axis, y_axis):
        self.action.scroll_by_amount(x_axis, y_axis).perform()

    # scrolling till the n(th) page is loaded
    def scroll_number_of_pages(self, number_of_pages):
        for _ in range(number_of_pages):
            element = self.driver.find_element(By.ID, 'DealsGridScrollAnchor')
            # Scroll to the bottom of the specific element
            self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
            time.sleep(2)  # Wait for items to load

    def add_item_to_cart(self):
        all_items = self.driver.find_elements(By.XPATH, "//button[text()='Add to Cart']")
        random_int = random.randint(0, len(all_items))
        all_items[random_int].click()
