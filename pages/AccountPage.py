from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LogoutPage import LogoutPage


class AccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.edit_your_account_link_text = (By.LINK_TEXT, "Edit your account information")
        self.logout_button_link_text = (By.LINK_TEXT, "Logout")

    def display_status_of_edit_your_account_information_option(self):
        return self.is_element_displayed(self.edit_your_account_link_text)

    def select_logout_button(self):
        self.click_on_element(self.logout_button_link_text)
        return LogoutPage(self.driver)