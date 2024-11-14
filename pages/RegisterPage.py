from selenium.webdriver.common.by import By

from pages.AccountSuccessPage import AccountSuccessPage
from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.NAME, "firstname")
        self.last_name = (By.ID, "input-lastname")
        self.email = (By.ID, "input-email")
        self.telephone = (By.ID, "input-telephone")
        self.password = (By.ID, "input-password")
        self.con_password = (By.ID, "input-confirm")
        self.yes_radio_button = (By.CSS_SELECTOR, "input[value='1'][name='newsletter']")
        self.privacy_policy_check_box = (By.CSS_SELECTOR, "input[name='agree']")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.duplicate_email_warning_xpath = (By.XPATH, "//div[@id='account-register']/div[1]")
        self.privacy_policy_warning_xpath = (By.XPATH, "//div[@id='account-register']/div[1]")
        self.first_name_warning_xpath = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
        self.last_name_warning_xpath = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
        self.email_warning_xpath = (By.XPATH, "//input[@id='input-email']/following-sibling::div")
        self.telephone_warning_xpath = (By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
        self.password_warning_xpath = (By.XPATH, "//input[@id='input-password']/following-sibling::div")

    def enter_first_name(self, first_name):
        self.send_keys_to_element(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.send_keys_to_element(self.last_name, last_name)

    def enter_email(self, email):
        self.send_keys_to_element(self.email, email)

    def enter_telephone(self, telephone):
        self.send_keys_to_element(self.telephone, telephone)

    def enter_password(self, password):
        self.send_keys_to_element(self.password, password)

    def enter_con_password(self, con_password):
        self.send_keys_to_element(self.con_password, con_password)

    def select_yes_radio_button(self):
        self.click_on_element(self.yes_radio_button)

    def check_mark_on_privacy_policy(self):
        self.click_on_element(self.privacy_policy_check_box)

    def click_on_continue_button(self):
        self.click_on_element(self.submit_button)
        return AccountSuccessPage(self.driver)

    def retrieve_duplicate_email_warning(self):
        return self.get_element_text(self.duplicate_email_warning_xpath)

    def retrieve_privacy_policy_warning(self):
        return self.get_element_text(self.privacy_policy_warning_xpath)

    def retrieve_first_name_warning(self):
        return self.get_element_text(self.first_name_warning_xpath)

    def retrieve_last_name_warning(self):
        return self.get_element_text(self.last_name_warning_xpath)

    def retrieve_email_warning(self):
        return self.get_element_text(self.email_warning_xpath)

    def retrieve_telephone_warning(self):
        return self.get_element_text(self.telephone_warning_xpath)

    def retrieve_password_warning(self):
        return self.get_element_text(self.password_warning_xpath)

    def verify_all_warnings(self, expected_privacy_policy_warning, expected_first_name_warning_message,
                            expected_last_name_warning_message, expected_email_warning_message,
                            expected_telephone_warning_message, expected_password_warning_message):
        actual_privacy_policy_warning = self.retrieve_privacy_policy_warning()
        actual_first_name_warning_message = self.retrieve_first_name_warning()
        actual_last_name_warning_message = self.retrieve_last_name_warning()
        actual_email_warning_message = self.retrieve_email_warning()
        actual_telephone_warning_message = self.retrieve_telephone_warning()
        actual_password_warning_message = self.retrieve_password_warning()

        status = False

        if expected_privacy_policy_warning.__eq__(actual_privacy_policy_warning):
            if expected_first_name_warning_message.__eq__(actual_first_name_warning_message):
                if expected_last_name_warning_message.__eq__(actual_last_name_warning_message):
                    if expected_email_warning_message.__eq__(actual_email_warning_message):
                        if expected_telephone_warning_message.__eq__(actual_telephone_warning_message):
                            if expected_password_warning_message.__eq__(actual_password_warning_message):
                                status = True

        return status
