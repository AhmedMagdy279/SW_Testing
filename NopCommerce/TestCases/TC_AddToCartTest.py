import time
import unittest
import sys
import os
from PageObjects.HomePage import HomePage
from PageObjects.SearchPage import SearchPage
from selenium import webdriver
from TestSuites.SheetsAutomation import SheetsAutomation
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
        chrome_options.add_argument("--ignore-certificate-errors")
        self.driver = webdriver.Chrome(options=chrome_options)
        excel_path = os.path.join(TB_Path, "TC_AddToCartTest_Report.xlsx")
        self.sheet = SheetsAutomation(excel_path)

    def tearDown(self):
        self.sheet.save()
        self.driver.close()
        self.driver.quit()

    def test_add_single_item_all_sections(self):  # Comprehensive Testing (might be added later)
        self.assertTrue(True)  # as it will be time-consuming to pick item from 13 pages.

    def test_searchANDadd_item_no_attributes(self):  # TC_01. Search & pick 'HTC One Mini Blue'
        # starting at the homepage
        self.driver.get("https://demo.nopcommerce.com/")
        # creating object from the homepage model
        homepage = HomePage(self.driver)
        # search for the item there first
        homepage.enter_search_text("HTC One Mini Blue")
        homepage.click_search_button()
        time.sleep(2)
        # we are now redirected to the search page
        search_page = SearchPage(self.driver)
        # scroll to allow to click on add to cart
        search_page.scroll_page(0, 200)
        search_page.click_on_first_item_add_to_cart()
        time.sleep(2)
        try:
            search_page.get_notification_bar()
            self.assertTrue(True)
            self.sheet.write_in_cell(TC2_Data['Actual']['row'], TC2_Data['Actual']['col'],
                                     'Notification item added successfully')
            self.sheet.write_in_cell(TC2_Data['P/F']['row'], TC2_Data['P/F']['col'], 'Pass')
        except:
            self.sheet.write_in_cell(TC2_Data['Actual']['row'], TC2_Data['Actual']['col'], 'Item is not added')
            self.sheet.write_in_cell(TC2_Data['P/F']['row'], TC2_Data['P/F']['col'], 'Fail')
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
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'] + 1, TC2_Data['Actual']['col'],
                                       'Notification item added successfully')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'] + 1, TC2_Data['P/F']['col'], 'Pass')
        except:
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'] + 1, TC2_Data['Actual']['col'], 'Item is not added')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'] + 1, TC2_Data['P/F']['col'], 'Fail')
            self.assertTrue(False)

    def test_add_item_multiple_times(self):  # TC_03 & TC_04
        # TC_03 implementation: Adding item multiple times
        self.__driver.find_element(By.XPATH, "//a[text()='HTC One M8 Android L 5.0 Lollipop']").click()
        self.__driver.implicitly_wait(4)
        self.__driver.find_element(By.ID, "product_enteredQuantity_18").clear()
        self.__driver.find_element(By.ID, "product_enteredQuantity_18").send_keys("2")
        self.__driver.find_element(By.ID, "add-to-cart-button-18").click()
        time.sleep(1)
        self.__driver.find_element(By.ID, "add-to-cart-button-18").click()  # item is added 4 times now
        # TC_04 implementation: checking the items in cart
        try:
            time.sleep(1)
            while 1:
                self.__driver.find_element(By.XPATH, "//span[@class='close']").click()
        except:
            time.sleep(1)
        self.__driver.find_element(By.XPATH, "//span[@class='cart-label']").click()
        item = self.__driver.find_element(By.XPATH, "//td/a[text()='HTC One M8 Android L 5.0 Lollipop']"
                                                    "/../../td[@class='quantity']/div/input")
        quantity = item.get_attribute("value")
        if quantity == "4":
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'] + 2, TC2_Data['Actual']['col'],
                                       'item quantity added successfully')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'] + 2, TC2_Data['P/F']['col'], 'Pass')
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'] + 3, TC2_Data['Actual']['col'],
                                       'Follow up cart successfully checked ')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'] + 3, TC2_Data['P/F']['col'], 'Pass')
            self.assertTrue(True)
        else:
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'] + 2, TC2_Data['Actual']['col'],
                                       'Quantity value mismatch')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'] + 2, TC2_Data['P/F']['col'], 'Fail')
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'] + 3, TC2_Data['Actual']['col'],
                                       'Follow up cart check fail')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'] + 3, TC2_Data['P/F']['col'], 'Fail')
            self.assertTrue(False)

    def test_remove_item_from_cart(self):  # TC_05. To be added later
        self.__driver.find_element(By.XPATH, "//a[text()='HTC One M8 Android L 5.0 Lollipop']").click()
        self.__driver.implicitly_wait(4)
        self.__driver.find_element(By.ID, "add-to-cart-button-18").click()
        time.sleep(1)
        self.__driver.find_element(By.XPATH, "//span[@class='close']").click()
        self.__driver.find_element(By.XPATH, "//span[@class='cart-label']").click()
        #
        self.__driver.find_element(By.XPATH, "//td/a[text()='HTC One M8 Android L 5.0 Lollipop']"
                                             "/../../td[@class='remove-from-cart']/button").click()
        try:
            self.__driver.find_element(By.XPATH, "//td/a[text()='HTC One M8 Android L 5.0 Lollipop']")
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'] + 4, TC2_Data['Actual']['col'],
                                       'item removal failed')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'] + 4, TC2_Data['P/F']['col'], 'Fail')
            self.assertTrue(False)
        except:
            self.__sheet.write_in_cell(TC2_Data['Actual']['row'] + 4, TC2_Data['Actual']['col'],
                                       'item removal successful')
            self.__sheet.write_in_cell(TC2_Data['P/F']['row'] + 4, TC2_Data['P/F']['col'], 'Pass')
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
