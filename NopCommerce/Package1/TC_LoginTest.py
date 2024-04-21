import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Suites.SheetsAutomation import SheetsAutomation

TC_Data = {'Email': {'row': 2, 'col': 3},
           'Password': {'row': 2, 'col': 4},
           'Actual': {'row': 2, 'col': 6},
           'P/F': {'row': 2, 'col': 7},
           'Comments': {'row': 2, 'col': 8}
           }


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.__driver = webdriver.Firefox()
        self.__driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")
        self.__sheet = SheetsAutomation('../Test_Suites/TC_LoginTest_Report.xlsx')
        self.Email_R = TC_Data['Email']['row']
        self.Email_C = TC_Data['Email']['row']
        self.Pass_R = TC_Data['Password']['row']
        self.Pass_C = TC_Data['Password']['row']
        self.ACT_R = TC_Data['Actual']['row']
        self.ACT_C = TC_Data['Actual']['row']
        self.PF_R = TC_Data['P/F']['row']
        self.PF_C = TC_Data['P/F']['row']

    def tearDown(self):
        self.__sheet.save()
        self.__driver.close()
        self.__driver.quit()

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
        email = self.__sheet.read_from_cell(TC_Data['Email']['row']+1, TC_Data['Email']['col'])
        password = self.__sheet.read_from_cell(TC_Data['Password']['row']+1, TC_Data['Password']['col'])
        self.__driver.find_element(By.ID, 'Email').send_keys(email)
        self.__driver.find_element(By.ID, 'Password').send_keys(password)
        self.__driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()
        self.__driver.implicitly_wait(5)
        try:
            if (self.__driver.current_url == "https://demo.nopcommerce.com/"
                    and self.__driver.find_element(By.XPATH, "//a[@class='ico-account']")):
                self.assertTrue(True)
            self.__sheet.write_in_cell(self.ACT_R+1, self.ACT_C, 'Successfully Navigated to Home page')
            self.__sheet.write_in_cell(self.PF_R+1, self.PF_C, 'Pass')
        except:
            if (self.__driver.current_url == "https://demo.nopcommerce.com/login?returnurl=%2F"
                    and self.__driver.find_element(By.XPATH,
                                                   "//div[@class='message-error validation-summary-errors']")):
                self.assertTrue(False)
            self.__sheet.write_in_cell(self.ACT_R+1, TC_Data['Actual']['col'], 'Failed to login')
            self.__sheet.write_in_cell(self.PF_R+1, self.PF_C, 'Fail')

    def test_invalidEmail_login_by_email(self):  # TC_03
        email = self.__sheet.read_from_cell(TC_Data['Email']['row']+2, TC_Data['Email']['col'])
        password = self.__sheet.read_from_cell(TC_Data['Password']['row']+2, TC_Data['Password']['col'])
        self.__driver.find_element(By.ID, 'Email').send_keys(email)
        self.__driver.find_element(By.ID, 'Password').send_keys(password)
        self.__driver.find_element(By.XPATH, "//button[@class='button-1 login-button']").click()
        self.__driver.implicitly_wait(5)
        try:
            if (self.__driver.current_url == "https://demo.nopcommerce.com/"
                    and self.__driver.find_element(By.XPATH, "//a[@class='ico-account']")):
                self.assertTrue(True)
            self.__sheet.write_in_cell(self.ACT_R+2, self.ACT_C, 'Successfully Navigated to Home page')
            self.__sheet.write_in_cell(self.PF_R+2, self.PF_C, 'Pass')
        except:
            if (self.__driver.current_url == "https://demo.nopcommerce.com/login?returnurl=%2F"
                    and self.__driver.find_element(By.XPATH,
                                                   "//div[@class='message-error validation-summary-errors']")):
                self.assertTrue(False)
            self.__sheet.write_in_cell(self.ACT_R+2, self.ACT_C, 'Failed to login')
            self.__sheet.write_in_cell(self.PF_R+2, self.PF_C, 'Fail')


if __name__ == '__main__':
    unittest.main()
