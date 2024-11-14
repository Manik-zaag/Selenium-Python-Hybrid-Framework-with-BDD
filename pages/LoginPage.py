from selenium.webdriver.common.by import By

from pages.AccountPage import AccountPage
from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.email_address_field_name = (By.NAME, "email")
        self.password_field_id = (By.NAME, "password")
        self.login_button_css_selector = (By.CSS_SELECTOR, "input[value='Login']")
        self.warning_message_xpath = (By.XPATH, "//div[@id='account-login']/div[1]")

    def enter_email_address(self, email_address_text):
        self.send_keys_to_element(self.email_address_field_name, email_address_text)

    def enter_password(self, password_text):
        self.send_keys_to_element(self.password_field_id, password_text)

    def click_on_login_button(self):
        self.click_on_element(self.login_button_css_selector)
        return AccountPage(self.driver)

    def retrieve_warning_message(self):
        return self.get_element_text(self.warning_message_xpath)
