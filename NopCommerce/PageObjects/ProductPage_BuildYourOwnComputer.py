from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BuildYourOwnComputer:
    def __init__(self, driver):
        self.driver = driver
        self.processor_drop_down = (By.ID, "product_attribute_1")
        self.ram_drop_down = (By.ID, "product_attribute_2")
        self.hdd_radio_btn_320GB = (By.ID, "product_attribute_3_6")
        self.hdd_radio_btn_400GB = (By.ID, "product_attribute_3_7")
        self.os_radio_btn_vista_home = (By.ID, "product_attribute_4_8")
        self.os_radio_btn_vista_premium = (By.ID, "product_attribute_4_9")
        self.sw_checkbox_addon_ms_office = (By.ID, "product_attribute_5_10")
        self.sw_checkbox_addon_adobe_reader = (By.ID, "product_attribute_5_11")
        self.sw_checkbox_addon_total_commander = (By.ID, "product_attribute_5_12")
        self.notification_bar = (By.CSS_SELECTOR, "[class*='bar-notification']")
        self.shopping_cart = (By.XPATH, "//span[@class='cart-label']")
        self.add_product_to_cart = (By.XPATH, "//button[text()='Add to cart']")

    def select_processor_attribute_by_text(self, visible_text):
        drp_dwn = Select(self.driver.find_element(*self.processor_drop_down))
        drp_dwn.select_by_visible_text(visible_text)

    def select_ram_attribute_by_text(self,visible_text):
        drp_dwn = Select(self.driver.find_element(*self.ram_drop_down))
        drp_dwn.select_by_visible_text(visible_text)

    def select_hdd_option(self, option: str):
        if option == '320GB':
            self.driver.find_element(*self.hdd_radio_btn_320GB).click()
        elif option == '400GB':
            self.driver.find_element(*self.hdd_radio_btn_400GB).click()
        else:
            raise ValueError("Invalid HDD option")

    def select_os_option(self, option: str):
        if option == 'Vista Home':
            self.driver.find_element(*self.os_radio_btn_vista_home).click()
        elif option == 'Vista Premium':
            self.driver.find_element(*self.os_radio_btn_vista_premium).click()
        else:
            raise ValueError("Invalid OS option")

    # the next two following functions are used for checking/unchecking add-ons for software options to be added
    # to the PC we are building
    def set_checkbox_state(self, checkbox_locator, state: bool):
        checkbox = self.driver.find_element(*checkbox_locator)
        if checkbox.is_selected() != state:
            checkbox.click()

    def set_addon_checkboxes(self, ms_office: bool, adobe_reader: bool, total_commander: bool):
        self.set_checkbox_state(self.sw_checkbox_addon_ms_office, ms_office)
        self.set_checkbox_state(self.sw_checkbox_addon_adobe_reader, adobe_reader)
        self.set_checkbox_state(self.sw_checkbox_addon_total_commander, total_commander)

    def get_notification_bar(self):
        return self.driver.find_element(*self.notification_bar)
