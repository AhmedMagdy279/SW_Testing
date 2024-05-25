import unittest
import sys
import os
from PageObjects.LoginPage import LoginPage
from selenium import webdriver
from TestSuites.SheetsAutomation import SheetsAutomation
from TestBase.TC_Data import TC0_Data
from pathlib import Path

parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "TestBase")


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
        excel_path = os.path.join(TB_Path, "TC_LoginTest_Report.xlsx")
        self.sheet = SheetsAutomation(excel_path)
        self.login_page = LoginPage(self.driver)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.sheet.save()
        self.driver.close()
        self.driver.quit()

    def test_valid_login_by_email(self):  # TC_01
        email = self.sheet.read_from_cell(TC0_Data['Email']['row'], TC0_Data['Email']['col'])
        password = self.sheet.read_from_cell(TC0_Data['Password']['row'], TC0_Data['Password']['col'])
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        self.driver.implicitly_wait(5)
        try:
            error_msg = self.login_page.get_error_message()
            print(error_msg.text)
            self.sheet.write_in_cell(TC0_Data['Actual']['row'], TC0_Data['Actual']['col'], 'Failed to login')
            self.sheet.write_in_cell(TC0_Data['P/F']['row'], TC0_Data['P/F']['col'], 'Fail')
            self.assertTrue(False)
        except:
            self.sheet.write_in_cell(TC0_Data['Actual']['row'], TC0_Data['Actual']['col'],
                                     'Login Successful and redirected to Signed-in Page')
            self.sheet.write_in_cell(TC0_Data['P/F']['row'], TC0_Data['P/F']['col'], 'Pass')
            self.assertTrue(True)

    def test_invalidPassword_login_by_email(self):  # TC_02
        email = self.sheet.read_from_cell(TC0_Data['Email']['row'] + 1, TC0_Data['Email']['col'])
        password = self.sheet.read_from_cell(TC0_Data['Password']['row'] + 1, TC0_Data['Password']['col'])
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        self.driver.implicitly_wait(5)
        try:
            error_msg = self.login_page.get_error_message()
            print(error_msg.text)
            self.assertTrue(True)
            self.sheet.write_in_cell(TC0_Data['Actual']['row'] + 1, TC0_Data['Actual']['col'], 'Failed to login')
            self.sheet.write_in_cell(TC0_Data['P/F']['row'] + 1, TC0_Data['P/F']['col'], 'Pass')

        except:
            self.assertTrue(False)
            self.sheet.write_in_cell(TC0_Data['Actual']['row'] + 1, TC0_Data['Actual']['col'],
                                     'Unexpected login with invalid email')
            self.sheet.write_in_cell(TC0_Data['P/F']['row'] + 1, TC0_Data['P/F']['col'], 'Fail')

    def test_invalidEmail_login_by_email(self):  # TC_03
        email = self.sheet.read_from_cell(TC0_Data['Email']['row'] + 2, TC0_Data['Email']['col'])
        password = self.sheet.read_from_cell(TC0_Data['Password']['row'] + 2, TC0_Data['Password']['col'])
        self.login_page.enter_email(email)
        self.login_page.enter_password(password)
        self.login_page.click_login()
        self.driver.implicitly_wait(5)
        try:
            error_msg = self.login_page.get_error_message()
            print(error_msg.text)
            self.assertTrue(True)
            self.sheet.write_in_cell(TC0_Data['Actual']['row'] + 2, TC0_Data['Actual']['col'], 'Failed to login')
            self.sheet.write_in_cell(TC0_Data['P/F']['row'] + 2, TC0_Data['P/F']['col'], 'Pass')

        except:
            self.assertTrue(False)
            self.sheet.write_in_cell(TC0_Data['Actual']['row'] + 2, TC0_Data['Actual']['col'],
                                     'Unexpected login with invalid email')
            self.sheet.write_in_cell(TC0_Data['P/F']['row'] + 2, TC0_Data['P/F']['col'], 'Fail')


if __name__ == '__main__':
    unittest.main()
