from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.account_creation_message_xpath = (By.XPATH, "//div[@id='content']/h1")

    def retrive_account_creation_message(self):
        return self.get_element_text(self.account_creation_message_xpath)