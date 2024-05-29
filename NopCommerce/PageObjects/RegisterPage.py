from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name_textbox = (By.ID, 'FirstName')
        self.last_name_textbox = (By.ID, 'LastName')
        self.email_textbox = (By.ID, 'Email')
        self.password_textbox = (By.ID, 'Password')
        self.confirm_password_textbox = (By.ID, 'ConfirmPassword')
        self.register_button = (By.ID, "register-button")
        self.register_success = (By.XPATH, "//div[text()='Your registration completed']")

    def enter_first_name(self, f_name):
        self.driver.find_element(*self.first_name_textbox).send_keys(f_name)

    def enter_last_name(self, l_name):
        self.driver.find_element(*self.last_name_textbox).send_keys(l_name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.driver.find_element(*self.confirm_password_textbox).send_keys(confirm_password)

    def click_register(self):
        self.driver.find_element(*self.register_button).click()

    def enter_all_register_info(self, fname, lname, email, password):
        self.enter_first_name(fname)
        self.enter_last_name(lname)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.click_register()

    def get_registration_status(self):
        if self.driver.find_element(*self.register_success):
            return True
        else:
            return False

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class*='error']")
