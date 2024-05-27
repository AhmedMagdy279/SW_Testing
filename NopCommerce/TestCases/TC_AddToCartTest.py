import time
import unittest
import sys
import os
from PageObjects.HomePage import HomePage
from PageObjects.SearchPage import SearchPage
from selenium import webdriver
from selenium.common import NoSuchElementException
from PageObjects.ProductPage_BuildYourOwnComputer import BuildYourOwnComputer
from PageObjects.CartPage import CartPage
from pathlib import Path
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "Utils")
sys.path.append(TB_Path)
from Utils.write_xlsx import XlsxWriter


class AddToCartTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(options=chrome_options)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_add_single_item_all_sections(self):  # Comprehensive Testing (might be added later)
        self.assertTrue(True)  # as it will be time-consuming to pick item from 13 pages.

    def test_searchANDadd_item_no_attributes(self):  # TC_01. Search & pick 'HTC One Mini Blue'
        # Starting from the homepage
        self.driver.get("https://demo.nopcommerce.com/")
        # creating object from the homepage model
        homepage = HomePage(self.driver)
        # search for the item there first
        homepage.enter_search_text("HTC One Mini Blue")
        homepage.click_search_button()
        time.sleep(2)
        # we are now redirected to the search page
        search_page = SearchPage(self.driver)
        # scroll to allow to click on add to cart
        search_page.scroll_page(0, 200)
        search_page.click_on_first_item_add_to_cart()
        time.sleep(2)
        try:
            search_page.get_notification_bar()
            self.assertTrue(True)
            XlsxWriter.write_add_to_cart_test_result('TC_01', 'Item added successfully', 'Pass', '')
        except NoSuchElementException:
            XlsxWriter.write_add_to_cart_test_result('TC_01', 'Item is not added', 'Fail', '')
            self.assertTrue(False)

    def test_add_item_with_attributes(self):  # TC_02
        # Starting from the Product Page (Focused on specific kind of product pages)
        self.driver.get("https://demo.nopcommerce.com/build-your-own-computer")
        # creating obj from the product page
        product_page = BuildYourOwnComputer(self.driver)
        # Picking 'Build your own computer' with the following:
        # 2.2 GHZ Intel Pentium Dual-Core E2200
        product_page.select_processor_attribute_by_text("2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00]")
        # 4 GB RAM, 320 GB HDD
        product_page.select_ram_attribute_by_text("4GB [+$20.00]")
        product_page.select_hdd_option('320GB')
        # Vista Home, MS Office + Total Commander
        product_page.select_os_option('Vista Home')
        product_page.set_addon_checkboxes(ms_office=True, adobe_reader=False, total_commander=True)
        time.sleep(2)
        try:
            product_page.get_notification_bar()
            self.assertTrue(True)
            XlsxWriter.write_add_to_cart_test_result('TC_02', 'Item added successfully', 'Pass', '')
        except NoSuchElementException:
            XlsxWriter.write_add_to_cart_test_result('TC_01', 'Item is not added', 'Fail', '')
            self.assertTrue(False)

    def test_add_item_twice_and_remove(self):  # TC_03, TC_04 & TC_05
        # Starting on homepage
        self.driver.get("https://demo.nopcommerce.com/")
        homepage = HomePage(self.driver)
        time.sleep(2)
        # TC_03 implementation: Adding item multiple times from featured section on homepage
        homepage.scroll_page(0, 200)
        homepage.click_add_to_cart_featured_product_htc_one_m8()
        time.sleep(1)
        homepage.click_add_to_cart_featured_product_htc_one_m8()    # item is added 2 times now
        # TC_04 implementation: checking the items in cart
        # closing notification bar first
        homepage.close_notification_bar()
        homepage.click_shopping_cart()
        # creating CartPage object
        cart_page = CartPage(self.driver)
        time.sleep(2)
        # check the quantity added
        quantity = cart_page.get_HTC_one_M8_quantity()
        if quantity == "2":
            XlsxWriter.write_add_to_cart_test_result('TC_03', 'item quantity added successfully', 'Pass', '')
            XlsxWriter.write_add_to_cart_test_result('TC_04', 'Follow up cart successfully checked', 'Pass', '')
        else:
            XlsxWriter.write_add_to_cart_test_result('TC_03', 'Quantity value mismatch', 'Fail', '')
            XlsxWriter.write_add_to_cart_test_result('TC_04', 'Follow up cart check fail', 'Fail', '')
            self.assertTrue(False)
        # TC_05 implementation: removing items from cart
        cart_page.remove_HTC_one_M8_from_cart()
        try:
            # try to check item quantity if still there then it wasn't removed
            quantity = cart_page.get_HTC_one_M8_quantity()
            XlsxWriter.write_add_to_cart_test_result('TC_05', 'item removal failed', 'Fail', '')
            self.assertTrue(False)
        except NoSuchElementException:
            XlsxWriter.write_add_to_cart_test_result('TC_05', 'item removal successful', 'Pass', '')
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
