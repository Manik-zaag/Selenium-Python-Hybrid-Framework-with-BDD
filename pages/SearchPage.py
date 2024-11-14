from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    valid_hp_product_link_text = (By.LINK_TEXT, "HP LP3065")
    no_product_message_xpath = (By.XPATH, "//div[@id='content']/p[2]")

    def display_status_of_valid_product(self):
        return self.is_element_displayed(self.valid_hp_product_link_text)

    def retrieve_no_product_message(self):
        return  self.get_element_text(self.no_product_message_xpath)
