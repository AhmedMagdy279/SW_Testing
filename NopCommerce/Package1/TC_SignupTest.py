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
        self.FName_R = TC1_Data['First']['row']
        self.FName_C = TC1_Data['First']['col']
        self.LName_R = TC1_Data['Last']['row']
        self.LName_C = TC1_Data['Last']['col']
        self.Email_R = TC1_Data['Email']['row']
        self.Email_C = TC1_Data['Email']['col']
        self.Pass_R = TC1_Data['Password']['row']
        self.Pass_C = TC1_Data['Password']['col']
        self.ACT_R = TC1_Data['Actual']['row']
        self.ACT_C = TC1_Data['Actual']['col']
        self.PF_R = TC1_Data['P/F']['row']
        self.PF_C = TC1_Data['P/F']['col']

    def tearDown(self):
        self.__sheet.save()
        self.__driver.close()
        self.__driver.quit()

    def test_valid_signup(self):  # TC_01
        f_name = self.__sheet.read_from_cell(self.FName_R, self.FName_C)
        l_name = self.__sheet.read_from_cell(self.LName_R, self.LName_C)
        email = self.__sheet.read_from_cell(self.Email_R, self.Email_C)
        password = self.__sheet.read_from_cell(self.Pass_R, self.Pass_C)
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
            self.__sheet.write_in_cell(self.ACT_R, self.ACT_C, 'Successfully Navigated to Home page')
            self.__sheet.write_in_cell(self.PF_R, self.PF_C, 'Pass')
        except:
            self.__sheet.write_in_cell(self.ACT_R, self.ACT_C, 'Failed to Sign up')
            self.__sheet.write_in_cell(self.PF_R, self.PF_C, 'Fail')
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
