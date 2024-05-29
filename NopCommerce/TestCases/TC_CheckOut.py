import time
import unittest
import sys
import os
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from PageObjects.RegisterPage import RegisterPage
from PageObjects.CartPage import CartPage
from PageObjects.CheckoutPage import CheckoutPage
from pathlib import Path
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "Utils")
sys.path.append(TB_Path)
from Utils.write_xlsx import XlsxWriter
from Utils.read_xlsx import XlsxReader


class BaseTest(unittest.TestCase):
    driver = None  # Explicitly declare the driver attribute at the class level

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        if cls.driver:
            cls.driver.quit()

    def register_and_login(self, user):
        self.driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Flogin")
        time.sleep(2)
        register = RegisterPage(self.driver)
        register.enter_all_register_info(user.f_name, user.l_name, user.email, user.password)
        time.sleep(1)
        self.driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
        time.sleep(2)
        login_page = LoginPage(self.driver)
        login_page.enter_credentials(user.email, user.password)
        time.sleep(1)

    def add_item_and_goto_cart(self):
        homepage = HomePage(self.driver)
        time.sleep(2)
        homepage.scroll_page(0, 200)
        homepage.click_add_to_cart_featured_product_htc_one_m8()
        time.sleep(1)
        homepage.close_notification_bar()
        homepage.click_shopping_cart()

    def goto_checkout(self):
        cart_page = CartPage(self.driver)
        time.sleep(1)
        cart_page.click_terms_of_service()
        cart_page.click_and_goto_checkout()

    def checkout_process(self, user):
        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_full_user_billing_data(user.f_name, user.l_name,
                                                   user.email, user.country, user.city,
                                                   user.address, user.zip, user.phone_number)
        checkout_page.navigate_to_shipment()
        checkout_page.select_shipment_option(user.shipping_method)
        checkout_page.navigate_to_payment_method()
        checkout_page.select_payment_option(user.payment_method)
        checkout_page.navigate_to_payment_info()
        checkout_page.navigate_to_checkout_info_overview()
        checkout_page.finalise_checkout()
        if checkout_page.check_order_status():
            return True
        else:
            return False


class RegisteredCheckoutTests(BaseTest):
    def setUp(self):
        users = XlsxReader.get_checkout_data()
        self.user = users['TC_01']  # Get the user for test case TC_01
        self.register_and_login(self.user)
        self.add_item_and_goto_cart()
        self.goto_checkout()

    def test_go_to_checkout_registered_account(self):
        if self.checkout_process(self.user):
            XlsxWriter.write_checkout_test_result('TC_01', 'order was successfully added', 'Pass', '')
            self.assertTrue(True)
        else:
            XlsxWriter.write_checkout_test_result('TC_01', 'Error to submit the order', 'Fail', '')
            self.assertTrue(False)


class GuestCheckoutTests(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://demo.nopcommerce.com/")
        users = XlsxReader.get_checkout_data()
        self.user = users['TC_03']  # Get the user for test case TC_03

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_go_to_checkout_as_a_guest(self):
        homepage = HomePage(self.driver)
        time.sleep(2)
        homepage.scroll_page(0, 200)
        homepage.click_add_to_cart_featured_product_htc_one_m8()
        time.sleep(1)
        homepage.close_notification_bar()
        homepage.click_shopping_cart()
        cart_page = CartPage(self.driver)
        time.sleep(1)
        cart_page.click_terms_of_service()
        cart_page.click_and_goto_checkout()
        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_full_user_billing_data(self.user.f_name, self.user.l_name,
                                                   self.user.email, self.user.country, self.user.city,
                                                   self.user.address, self.user.zip, self.user.phone_number)
        checkout_page.navigate_to_shipment()
        checkout_page.select_shipment_option(self.user.shipping_method)
        checkout_page.navigate_to_payment_method()
        checkout_page.select_payment_option(self.user.payment_method)
        checkout_page.navigate_to_payment_info()
        checkout_page.navigate_to_checkout_info_overview()
        checkout_page.finalise_checkout()
        if checkout_page.check_order_status():
            XlsxWriter.write_checkout_test_result('TC_03', 'order was successfully added', 'Pass', '')
            self.assertTrue(True)
        else:
            XlsxWriter.write_checkout_test_result('TC_03', 'Error to submit the order', 'Fail', '')
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
