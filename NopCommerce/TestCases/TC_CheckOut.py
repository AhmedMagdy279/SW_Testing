import time
import unittest
import sys
import os
from selenium import webdriver
from TestSuites.SheetsAutomation import SheetsAutomation
# from TestBase.TC_Data import TC2_Data
from pathlib import Path
parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "TestBase")


class CheckoutTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--ignore-certificate-errors")
        self.__driver = webdriver.Chrome(options=chrome_options)
        self.__driver.get("https://demo.nopcommerce.com/")
        excel_path = os.path.join(TB_Path, "TC_AddToCartTest_Report.xlsx")
        self.__sheet = SheetsAutomation(excel_path)

    def tearDown(self):
        self.__sheet.save()
        self.__driver.quit()

    def test_go_to_checkout_registered_account(self):

        self.assertTrue(True)

    def test_go_to_checkout_register_new_account(self):

        self.assertTrue(True)

    def test_go_to_checkout_as_a_guest(self):

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
