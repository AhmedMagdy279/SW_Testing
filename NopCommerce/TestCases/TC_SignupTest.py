import time
import unittest
from selenium.common import NoSuchElementException
from PageObjects.RegisterPage import RegisterPage
from selenium import webdriver
from pathlib import Path
import os
import sys
from pathlib import Path
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "Utils")
sys.path.append(TB_Path)
from Utils.read_xlsx import XlsxReader
from Utils.write_xlsx import XlsxWriter


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Flogin")
        self.register_page = RegisterPage(self.driver)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test01_valid_signup(self):  # TC_01
        users = XlsxReader.get_signup_data()
        user = users['TC_01']  # get the user for test case TC_01
        self.register_page.enter_first_name(user.f_name)
        self.register_page.enter_last_name(user.l_name)
        self.register_page.enter_email(user.email)
        self.register_page.enter_password(user.password)
        self.register_page.enter_confirm_password(user.password)
        self.register_page.click_register()
        time.sleep(2)
        try:
            self.register_page.get_registration_status()
            self.assertTrue(True)
            XlsxWriter.write_signup_test_result('TC_01', 'Successfully Navigated to Home page', 'Pass', '')
        except NoSuchElementException:
            XlsxWriter.write_signup_test_result('TC_01',
                                                'Failed to Sign up',
                                                'Fail',
                                                'The registration of the same account was made recently. Try later or '
                                                'change credentials')
            self.assertTrue(False)

    def test02_invalid_signup(self):  # TC_02
        users = XlsxReader.get_signup_data()
        user = users['TC_02']  # get the user for test case TC_02
        self.register_page.enter_first_name(user.f_name)
        self.register_page.enter_last_name(user.l_name)
        self.register_page.enter_email(user.email)
        self.register_page.enter_password(user.password)
        self.register_page.enter_confirm_password(user.password)
        self.register_page.click_register()
        self.driver.implicitly_wait(5)
        try:
            self.register_page.get_registration_status()
            XlsxWriter.write_signup_test_result('TC_02', 'Unexpected! register succeeded', 'Fail', '')
            self.assertTrue(False)
        except NoSuchElementException:
            self.assertTrue(True)
            XlsxWriter.write_signup_test_result('TC_02', 'Error registering as the email already used', 'Pass', '')


if __name__ == '__main__':
    unittest.main()
