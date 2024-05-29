from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common import NoSuchElementException



class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_textbox = (By.ID, "small-searchterms")
        self.search_button = (By.XPATH, "//button[text()='Search']")
        self.first_name_input = (By.ID, "BillingNewAddress_FirstName")
        self.last_name_input = (By.ID, "BillingNewAddress_LastName")
        self.email_input = (By.ID, "BillingNewAddress_Email")
        self.country_drop_down = (By.ID, "BillingNewAddress_CountryId")
        self.city_name_input = (By.ID, "BillingNewAddress_City")
        self.address_input = (By.ID, "BillingNewAddress_Address1")
        self.zipcode_input = (By.ID, "BillingNewAddress_ZipPostalCode")
        self.phone_number_input = (By.ID, "BillingNewAddress_PhoneNumber")
        self.billing_continue_btn = (By.XPATH, "//div[@id='billing-buttons-container']//button[@name='save']")
        self.ground_shipping_btn = (By.ID, "shippingoption_0")
        self.next_day_air_shipping_btn = (By.ID, "shippingoption_1")
        self.second_day_air_shipping_btn = (By.ID, "shippingoption_2")
        self.shipping_continue_btn = (By.XPATH, "//div[@id='shipping-method-buttons-container']//button")
        self.payment_check_btn = (By.ID, "paymentmethod_0")
        self.payment_card_btn = (By.ID, "paymentmethod_1")
        self.payment_continue_btn = (By.XPATH, "//div[@id='payment-method-buttons-container']//button[@name='save']")
        self.payment_info_continue_btn = (By.XPATH, "//div[@id='payment-info-buttons-container']//button")
        self.confirm_checkout = (By.XPATH, "//div[@id='confirm-order-buttons-container']//button")
        self.order_success_text = (By.XPATH, "//strong[text()='Your order has been successfully processed!']")

    def enter_full_user_billing_data(self, f_name, l_name, email, country, city, address, zipPostal, phone_number):
        self.driver.find_element(*self.first_name_input).clear()
        self.driver.find_element(*self.last_name_input).clear()
        self.driver.find_element(*self.email_input).clear()
        self.driver.find_element(*self.first_name_input).send_keys(f_name)
        self.driver.find_element(*self.last_name_input).send_keys(l_name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.city_name_input).send_keys(city)
        self.driver.find_element(*self.address_input).send_keys(address)
        self.driver.find_element(*self.zipcode_input).send_keys(zipPostal)
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)
        country_dropdown_element = self.driver.find_element(*self.country_drop_down)
        select = Select(country_dropdown_element)
        select.select_by_visible_text(country)

    def enter_registered_user_billing_data(self, country, city, address, zipPostal, phone_number):
        self.driver.find_element(*self.city_name_input).send_keys(city)
        self.driver.find_element(*self.address_input).send_keys(address)
        self.driver.find_element(*self.zipcode_input).send_keys(zipPostal)
        self.driver.find_element(*self.phone_number_input).send_keys(phone_number)
        country_dropdown_element = self.driver.find_element(*self.country_drop_down)
        select = Select(country_dropdown_element)
        select.select_by_visible_text(country)

    def navigate_to_shipment(self):
        self.driver.find_element(*self.billing_continue_btn).click()

    def select_shipment_option(self, shipment):
        if "2nd Day Air" in shipment:
            self.driver.find_element(*self.second_day_air_shipping_btn).click()
        elif "Next Day Air" in shipment:
            self.driver.find_element(*self.next_day_air_shipping_btn).click()
        else:
            self.driver.find_element(*self.ground_shipping_btn).click()

    def navigate_to_payment_method(self):
        self.driver.find_element(*self.shipping_continue_btn).click()

    def select_payment_option(self, payment):
        if "Card" in payment:
            self.driver.find_element(*self.payment_card_btn).click()
        else:
            self.driver.find_element(*self.payment_check_btn).click()

    def navigate_to_payment_info(self):
        self.driver.find_element(*self.payment_continue_btn).click()

    def navigate_to_checkout_info_overview(self):
        self.driver.find_element(*self.payment_info_continue_btn).click()

    def finalise_checkout(self):
        self.driver.find_element(*self.confirm_checkout).click()

    def check_order_status(self):
        try:
            if (self.driver.find_element(*self.order_success_text).text()
                    == "Your order has been successfully processed!"):
                return True
        except NoSuchElementException:
            return False
