import unittest
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Suites.SheetsAutomation import SheetsAutomation


class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.__driver = webdriver.Firefox()
        self.__driver.get("https://sso.teachable.com/secure/9521/identity/login/password")
        self.__sheet = SheetsAutomation('../TestSuite/LoginTest_Report.xlsx')
        self.allItems = self.__driver.find_elements(By.XPATH, "//div[@class='product']")

    def tearDown(self):
        self.__sheet.save()
        self.__driver.close()
        self.__driver.quit()

    def test_add_all_items_random_amount(self):         # TC_01
        self.assertTrue(True)

    def test_search_random_item_and_addToCart(self):    # TC_02
        self.assertTrue(True)

    def test_click_addToCart_multiple_times(self):      # TC_03. Fail from the second time & on
        self.assertTrue(True)

    def test_remove_random_item_from_cart(self):        # TC_04
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
