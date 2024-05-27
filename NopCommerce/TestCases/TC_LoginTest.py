import unittest
from selenium.common import NoSuchElementException
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
import os
import sys
from pathlib import Path

parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "Utils")
sys.path.append(TB_Path)
from Utils.read_xlsx import XlsxReader
from Utils.write_xlsx import XlsxWriter


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
        self.login_page = LoginPage(self.driver)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_valid_login_by_email(self):  # TC_01
        users = XlsxReader.get_login_data()
        user = users['TC_01']  # get the user for test case TC_01
        self.login_page.enter_email(user.email)
        self.login_page.enter_password(user.password)
        self.login_page.click_login()
        self.driver.implicitly_wait(5)
        try:
            error_msg = self.login_page.get_error_message()
            print(error_msg.text)
            XlsxWriter.write_login_test_result('TC_01', error_msg.text, 'Fail',
                                               'To pass this you need to register the account with same credentials '
                                               'first')
            self.assertTrue(False)
        except NoSuchElementException:
            # this block will be executed if no error message is found
            XlsxWriter.write_login_test_result('TC_01', 'login successful', 'Pass', '')
            self.assertTrue(True)

    def test_invalidPassword_login_by_email(self):  # TC_02
        users = XlsxReader.get_login_data()
        user = users['TC_02']  # get the user for test case TC_01
        self.login_page.enter_email(user.email)
        self.login_page.enter_password(user.password)
        self.login_page.click_login()
        self.driver.implicitly_wait(5)
        try:
            error_msg = self.login_page.get_error_message()
            print(error_msg.text)
            self.assertTrue(True)
            XlsxWriter.write_login_test_result('TC_02', error_msg.text, 'Pass', '')
        except NoSuchElementException:
            # this block will be executed if no error message is found
            self.assertTrue(False)
            XlsxWriter.write_login_test_result('TC_01',
                                               'unexpected login successful with invalid email',
                                               'Fail',
                                               '')

    def test_invalidEmail_login_by_email(self):  # TC_03
        users = XlsxReader.get_login_data()
        user = users['TC_03']  # get the user for test case TC_01
        self.login_page.enter_email(user.email)
        self.login_page.enter_password(user.password)
        self.login_page.click_login()
        self.driver.implicitly_wait(5)
        try:
            error_msg = self.login_page.get_error_message()
            print(error_msg.text)
            self.assertTrue(True)
            XlsxWriter.write_login_test_result('TC_03', error_msg.text, 'Pass', '')
        except NoSuchElementException:
            # this block will be executed if no error message is found
            self.assertTrue(False)
            XlsxWriter.write_login_test_result('TC_03',
                                               'unexpected login successful with invalid email',
                                               'Fail',
                                               '')


if __name__ == '__main__':
    unittest.main()
