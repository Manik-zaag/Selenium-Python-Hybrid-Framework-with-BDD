from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LogoutPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.account_logout_title_xpath = (By.XPATH, "//div[@id='content']/h1")

    def account_logout_title_is_displayed(self):
        return self.is_element_displayed(self.account_logout_title_xpath)

