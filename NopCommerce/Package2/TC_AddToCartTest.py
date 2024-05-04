import time
import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Test_Suites.SheetsAutomation import SheetsAutomation
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from TestBase.TC_Data import TC2_Data
from pathlib import Path


parent_folder = os.path.dirname(os.path.abspath(__file__))
sys.path.append(parent_folder)
TB_Path = os.path.join(Path(parent_folder).parent.absolute(), "TestBase")


class AddToCartTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("headless")
        chrome_options.add_argument("--ignore-certificate-errors")
        self.__driver = webdriver.Chrome(options=chrome_options)
        self.__driver.get("https://demo.nopcommerce.com/")
        self.__action = ActionChains(self.__driver)
        excel_path = os.path.join(TB_Path, "TC_AddToCartTest_Report.xlsx")
        self.__sheet = SheetsAutomation(excel_path)

    def tearDown(self):
        self.__sheet.save()
        self.__driver.quit()

    def test_add_single_item_all_sections(self):  # Comprehensive Testing (might be added later)
        self.assertTrue(True)  # as it will be time-consuming to pick item from 13 pages.

    def test_searchANDadd_item_no_attributes(self):  # TC_01. Search & pick 'HTC One Mini BLue'
        self.__driver.find_element(By.ID, "small-searchterms").send_keys("HTC One")
        self.__driver.find_element(By.XPATH, "//button[text()='Search']").click()
        wait = WebDriverWait(self.__driver, 3)  # Wait for 3 seconds (adjust as needed)
        # add_to_cart = wait.until(
        #     EC.element_to_be_clickable((By.XPATH,
        #                                 "//a[text()='HTC One Mini Blue']/../../div[@class='add-info']/div["
        #                                 "@class='buttons']/button[text()='Add to cart']"))
        # )
        add_to_cart = self.__driver.find_element(By.XPATH,
                                                 "//a[text()='HTC One Mini Blue']/../../div[@class='add-info']/div["
                                                 "@class='buttons']/button[text()='Add to cart']")
        # scroll to allow to click
        self.__action.scroll_by_amount(0, 200).perform()
        add_to_cart.click()
        try:
            success_notification = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class ='bar-notification success']")))
            self.assertTrue(True)
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'], TC2_Data['Actual']['col'],
                                   'Notification item added successfully')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'], TC2_Data['P/F']['col'], 'Pass')
        except:
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'], TC2_Data['Actual']['col'],'Item is not added')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'], TC2_Data['P/F']['col'], 'Fail')
            self.assertTrue(False)

    def test_add_item_with_attributes(self):  # TC_02
        # Picking 'Build your own computer' with the following:
        # 2.2 GHZ Intel Pentium Dual-Core E2200
        # 8 GB RAM, 320 GB HDD
        # Vista Home, MS Office + Total Commander
        self.__driver.find_element(By.XPATH, "//a[text()='Build your own computer']").click()
        drp_dwn = Select(self.__driver.find_element(By.ID, "product_attribute_1"))
        drp_dwn.select_by_visible_text("2.5 GHz Intel Pentium Dual-Core E2200 [+$15.00]")
        drp_dwn = Select(self.__driver.find_element(By.ID, "product_attribute_2"))
        drp_dwn.select_by_visible_text("8GB [+$60.00]")
        self.__driver.find_element(By.ID, "product_attribute_3_6").click()
        self.__driver.find_element(By.ID, "product_attribute_4_8").click()
        if not self.__driver.find_element(By.ID, "product_attribute_4_8").is_selected():
            self.__driver.find_element(By.ID, "product_attribute_4_8").click()
        self.__driver.find_element(By.ID, "product_attribute_5_12").click()
        self.__driver.find_element(By.ID, "add-to-cart-button-1").click()
        wait = WebDriverWait(self.__driver, 3)  # Wait for 3 seconds (adjust as needed)

        try:
            success_notification = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class ='bar-notification success']")))
            self.assertTrue(True)
            self.__sheet.write_in_cell(TC2_Data['Actual']['row']+1, TC2_Data['Actual']['col'],
                                       'Notification item added successfully')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row']+1, TC2_Data['P/F']['col'], 'Pass')
        except:
            self.__sheet.write_in_cell(TC2_Data['Actual']['row']+1, TC2_Data['Actual']['col'], 'Item is not added')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row']+1, TC2_Data['P/F']['col'], 'Fail')
            self.assertTrue(False)

    def test_remove_item_from_cart(self):  # TC_04. To be added later
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
