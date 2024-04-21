import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Suites.SheetsAutomation import SheetsAutomation
from TestBase.TC_Data import TC0_Data
from pathlib import Path
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "TestBase")


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.__driver = webdriver.Firefox()
        self.__driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
        excel_path = os.path.join(TB_Path, "TC_LoginTest_Report.xlsx")
        self.__sheet = SheetsAutomation(excel_path)
        self.Email_R = TC0_Data['Email']['row']
        self.Email_C = TC0_Data['Email']['col']
        self.Pass_R = TC0_Data['Password']['row']
        self.Pass_C = TC0_Data['Password']['col']
        self.ACT_R = TC0_Data['Actual']['row']
        self.ACT_C = TC0_Data['Actual']['col']
        self.PF_R = TC0_Data['P/F']['row']
        self.PF_C = TC0_Data['P/F']['col']

    def test_valid_login_by_email(self):  # TC_01
        email = self.__sheet.read_from_cell(self.Email_R, self.Email_C)
        password = self.__sheet.read_from_cell(self.Pass_R, self.Pass_C)
        self.__driver.find_element(By.ID, 'Email').send_keys(email)
        self.__driver.find_element(By.ID, 'Password').send_keys(password)
        self.__driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()
        self.__driver.implicitly_wait(5)
        try:
            if (self.__driver.current_url == "https://demo.nopcommerce.com/"
                    and self.__driver.find_element(By.XPATH, "//a[@class='ico-account']")):
                self.assertTrue(True)
            self.__sheet.write_in_cell(self.ACT_R, self.ACT_C,
                                       'Registration Successful and redirected to Login Page')
            self.__sheet.write_in_cell(self.PF_R, self.PF_C, 'Pass')
        except:
            self.__sheet.write_in_cell(self.ACT_R, self.ACT_C, 'Failed to login')
            self.__sheet.write_in_cell(self.PF_R, self.PF_C, 'Fail')
            self.assertTrue(False)

    def test_invalidPassword_login_by_email(self):  # TC_02
        email = self.__sheet.read_from_cell(self.Email_R+1, self.Email_C)
        password = self.__sheet.read_from_cell(self.Pass_R+1, self.Pass_C)
        self.__driver.find_element(By.ID, 'Email').send_keys(email)
        self.__driver.find_element(By.ID, 'Password').send_keys(password)
        self.__driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()
        self.__driver.implicitly_wait(5)
        try:
            if (self.__driver.find_element(By.XPATH, "//a[@class='ico-account']")
                    and self.__driver.current_url == "https://demo.nopcommerce.com/"):
                self.assertTrue(False)
            self.__sheet.write_in_cell(self.ACT_R + 1, self.ACT_C, 'Unexpected login with invalid email')
            self.__sheet.write_in_cell(self.PF_R + 1, self.PF_C, 'Fail')
        except:
            if (self.__driver.current_url == "https://demo.nopcommerce.com/login?returnurl=%2F"
                    and self.__driver.find_element(By.XPATH,
                                                   "//div[@class='message-error validation-summary-errors']")):
                self.assertTrue(True)
            self.__sheet.write_in_cell(self.ACT_R + 1, self.ACT_C, 'Failed to login')
            self.__sheet.write_in_cell(self.PF_R + 1, self.PF_C, 'Pass')

    def test_invalidEmail_login_by_email(self):  # TC_03
        email = self.__sheet.read_from_cell(self.Email_R + 2, self.Email_C)
        password = self.__sheet.read_from_cell(self.Pass_R + 2, self.Pass_C)
        self.__driver.find_element(By.ID, 'Email').send_keys(email)
        self.__driver.find_element(By.ID, 'Password').send_keys(password)
        self.__driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()
        self.__driver.implicitly_wait(5)
        try:
            if (self.__driver.find_element(By.XPATH, "//a[@class='ico-account']")
                    and self.__driver.current_url == "https://demo.nopcommerce.com/"):
                print(self.__driver.current_url)
                self.assertTrue(False)
            self.__sheet.write_in_cell(self.ACT_R+2, self.ACT_C, 'Unexpected login with invalid email')
            self.__sheet.write_in_cell(self.PF_R+2, self.PF_C, 'Fail')
        except:
            if (self.__driver.current_url == "https://demo.nopcommerce.com/login?returnurl=%2F"
                    and self.__driver.find_element(By.XPATH,
                                                   "//div[@class='message-error validation-summary-errors']")):
                print(self.__driver.current_url)
                self.assertTrue(True)
            self.__sheet.write_in_cell(self.ACT_R+2, self.ACT_C, 'Failed to login')
            self.__sheet.write_in_cell(self.PF_R+2, self.PF_C, 'Pass')

    def tearDown(self):
        self.__sheet.save()
        self.__driver.close()
        self.__driver.quit()


if __name__ == '__main__':
    unittest.main()
