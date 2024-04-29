import unittest
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Suites.SheetsAutomation import SheetsAutomation
from TestBase.TC_Data import TC1_Data
from pathlib import Path
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "TestBase")


class SignupTest(unittest.TestCase):
    def setUp(self):
        self.__driver = webdriver.Firefox()
        self.__driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Flogin")
        excel_path = os.path.join(TB_Path, "TC_SignupTest_Report.xlsx")
        self.__sheet = SheetsAutomation(excel_path)

    def tearDown(self):
        self.__sheet.save()
        self.__driver.close()
        self.__driver.quit()

    def test_valid_signup(self):  # TC_01
        f_name = self.__sheet.read_from_cell(TC1_Data['FName']['row'], TC1_Data['FName']['col'])
        l_name = self.__sheet.read_from_cell(TC1_Data['LName']['row'], TC1_Data['LName']['col'])
        email = self.__sheet.read_from_cell(TC1_Data['Email']['row'], TC1_Data['Email']['col'])
        password = self.__sheet.read_from_cell(TC1_Data['Password']['row'], TC1_Data['Password']['col'])
        self.__driver.find_element(By.ID, 'FirstName').send_keys(f_name)
        self.__driver.find_element(By.ID, 'LastName').send_keys(l_name)
        self.__driver.find_element(By.ID, 'Email').send_keys(email)
        self.__driver.find_element(By.ID, 'Password').send_keys(password)
        self.__driver.find_element(By.ID, 'ConfirmPassword').send_keys(password)
        self.__driver.find_element(By.ID, "register-button").click()
        self.__driver.implicitly_wait(5)
        try:
            if self.__driver.current_url == "https://demo.nopcommerce.com/registerresult/1?returnUrl=/login":
                self.assertTrue(True)
            self.__driver.find_element(By.XPATH, "//a[@class='button-1 register-continue-button']").click()
            self.__sheet.write_in_cell(TC1_Data['Actual']['row'], TC1_Data['Actual']['col'], 'Successfully Navigated to Home page')
            self.__sheet.write_in_cell(TC1_Data['P/F']['row'], TC1_Data['P/F']['col'], 'Pass')
        except:
            self.__sheet.write_in_cell(TC1_Data['Actual']['row'], TC1_Data['Actual']['col'], 'Failed to Sign up')
            self.__sheet.write_in_cell(TC1_Data['P/F']['row'], TC1_Data['P/F']['col'], 'Fail')
            self.assertTrue(False)

    def test_invalid_signup(self):  # TC_02
        f_name = self.__sheet.read_from_cell(TC1_Data['FName']['row']+1, TC1_Data['FName']['col'])
        l_name = self.__sheet.read_from_cell(TC1_Data['LName']['row']+1, TC1_Data['LName']['col'])
        email = self.__sheet.read_from_cell(TC1_Data['Email']['row']+1, TC1_Data['Email']['col'])
        password = self.__sheet.read_from_cell(TC1_Data['Password']['row']+1, TC1_Data['Password']['col'])
        self.__driver.find_element(By.ID, 'FirstName').send_keys(f_name)
        self.__driver.find_element(By.ID, 'LastName').send_keys(l_name)
        self.__driver.find_element(By.ID, 'Email').send_keys(email)
        self.__driver.find_element(By.ID, 'Password').send_keys(password)
        self.__driver.find_element(By.ID, 'ConfirmPassword').send_keys(password)
        self.__driver.find_element(By.ID, "register-button").click()
        self.__driver.implicitly_wait(5)
        try:
            if (self.__driver.current_url == "https://demo.nopcommerce.com/register?returnurl=%2Flogin"
                    and self.__driver.find_element(By.XPATH, "//li[text()='The specified email already exists']")):
                self.assertTrue(True)
            self.__sheet.write_in_cell(TC1_Data['Actual']['row']+1, TC1_Data['Actual']['col'],
                                       'Error sign. Email already registered with another account')
            self.__sheet.write_in_cell(TC1_Data['P/F']['row']+1, TC1_Data['P/F']['col'], 'Pass')
        except:
            if self.__driver.current_url == "https://demo.nopcommerce.com/registerresult/1?returnUrl=/login":
                self.assertTrue(False)
            self.__sheet.write_in_cell(TC1_Data['Actual']['row']+1, TC1_Data['Actual']['col'], 'Unexpectedly Signed up')
            self.__sheet.write_in_cell(TC1_Data['P/F']['row']+1, TC1_Data['P/F']['col'], 'Fail')


if __name__ == '__main__':
    unittest.main()
