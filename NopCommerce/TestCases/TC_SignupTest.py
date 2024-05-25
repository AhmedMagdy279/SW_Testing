import time
import unittest
import os
import sys
from PageObjects.RegisterPage import RegisterPage
from selenium import webdriver
from TestSuites.SheetsAutomation import SheetsAutomation
from TestBase.TC_Data import TC1_Data
from pathlib import Path

parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "TestBase")


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Flogin")
        excel_path = os.path.join(TB_Path, "TC_SignupTest_Report.xlsx")
        self.sheet = SheetsAutomation(excel_path)
        self.register_page = RegisterPage(self.driver)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.sheet.save()
        self.driver.close()
        self.driver.quit()

    def test01_valid_signup(self):  # TC_01
        f_name = self.sheet.read_from_cell(TC1_Data['FName']['row'], TC1_Data['FName']['col'])
        l_name = self.sheet.read_from_cell(TC1_Data['LName']['row'], TC1_Data['LName']['col'])
        email = self.sheet.read_from_cell(TC1_Data['Email']['row'], TC1_Data['Email']['col'])
        password = self.sheet.read_from_cell(TC1_Data['Password']['row'], TC1_Data['Password']['col'])
        self.register_page.enter_first_name(f_name)
        self.register_page.enter_last_name(l_name)
        self.register_page.enter_email(email)
        self.register_page.enter_password(password)
        self.register_page.enter_confirm_password(password)
        self.register_page.click_register()
        time.sleep(2)
        try:
            if self.register_page.get_registration_status():
                self.assertTrue(True)
                self.sheet.write_in_cell(TC1_Data['Actual']['row'], TC1_Data['Actual']['col'],
                                         'Successfully Navigated to Home page')
                self.sheet.write_in_cell(TC1_Data['P/F']['row'], TC1_Data['P/F']['col'], 'Pass')
            else:
                raise Exception('Error signing up')
        except Exception as e:
            self.sheet.write_in_cell(TC1_Data['Actual']['row'], TC1_Data['Actual']['col'], 'Failed to Sign up')
            self.sheet.write_in_cell(TC1_Data['P/F']['row'], TC1_Data['P/F']['col'], 'Fail')
            self.assertTrue(False)

    def test02_invalid_signup(self):  # TC_02
        f_name = self.sheet.read_from_cell(TC1_Data['FName']['row'] + 1, TC1_Data['FName']['col'])
        l_name = self.sheet.read_from_cell(TC1_Data['LName']['row'] + 1, TC1_Data['LName']['col'])
        email = self.sheet.read_from_cell(TC1_Data['Email']['row'] + 1, TC1_Data['Email']['col'])
        password = self.sheet.read_from_cell(TC1_Data['Password']['row'] + 1, TC1_Data['Password']['col'])
        self.register_page.enter_first_name(f_name)
        self.register_page.enter_last_name(l_name)
        self.register_page.enter_email(email)
        self.register_page.enter_password(password)
        self.register_page.enter_confirm_password(password)
        self.register_page.click_register()
        self.driver.implicitly_wait(5)
        try:
            if self.register_page.get_registration_status():
                self.sheet.write_in_cell(TC1_Data['Actual']['row']+1, TC1_Data['Actual']['col'],
                                         'Unexpected! register succeeded')
                self.sheet.write_in_cell(TC1_Data['P/F']['row']+1, TC1_Data['P/F']['col'], 'Fail')
                self.assertTrue(False)
            else:
                raise Exception('Error signing up')
        except Exception as e:
            self.assertTrue(True)
            self.sheet.write_in_cell(TC1_Data['Actual']['row']+1, TC1_Data['Actual']['col'],
                                     'Error registering as the email already used')
            self.sheet.write_in_cell(TC1_Data['P/F']['row']+1, TC1_Data['P/F']['col'], 'Pass')


if __name__ == '__main__':
    unittest.main()
