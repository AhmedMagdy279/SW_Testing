from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_textbox = (By.ID, "Email")
        self.password_textbox = (By.ID, "Password")
        self.login_button = (By.XPATH, "//button[@class='button-1 login-button']")

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def enter_credentials(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class*='error']")

