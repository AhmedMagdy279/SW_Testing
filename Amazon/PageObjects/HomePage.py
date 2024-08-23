import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart = (By.ID, "nav-cart")
        self.search_textbox = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")
        self.today_deals_button = (By.XPATH, "//div[@id='nav-xshop']/a")
        self.item_added_notification = (By.XPATH, "//strong[text()='Item Added']")
        self.action = ActionChains(self.driver)

    def search_for_item(self, search_item):
        self.driver.find_element(*self.search_textbox).send_keys(search_item)
        self.driver.find_element(*self.search_button).click()
        time.sleep(2)

    def select_item_index_to_cart(self, item_number):
        all_items = self.driver.find_elements(By.XPATH, "//button[text()='Add to cart']")
        all_items[item_number-1].click()
        items_names = self.driver.find_elements(By.XPATH, "//h2/a/span")
        return items_names[item_number-1].text

    def go_to_today_deals_page(self):
        try:
            self.driver.find_element(By.XPATH, "//div[@class='glow-toaster-footer']/span/span").click()
        except Exception as e:
           print('nothing to be dismissed')
        self.driver.find_element(*self.today_deals_button).click()
        time.sleep(2)

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
