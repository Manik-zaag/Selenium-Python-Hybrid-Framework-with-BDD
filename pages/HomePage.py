from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.search_box_field_name = (By.NAME, "search")
        self.search_button_xpath = (By.XPATH, "//button[@class='btn btn-default btn-lg']")
        self.my_account_drop_menu_xpath = (By.XPATH, "//span[text()='My Account']")
        self.login_option_link_text = (By.LINK_TEXT, "Login")
        self.register_option_link_text = (By.LINK_TEXT, "Register")

    def retrieve_page_title(self):
        return self.get_page_title()

    def enter_product_into_search_box_field(self, product_name):
        self.send_keys_to_element(self.search_box_field_name, product_name)

    def click_on_search_button(self):
        self.click_on_element(self.search_button_xpath)
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.click_on_element(self.my_account_drop_menu_xpath)

    def select_login_option(self):
        self.click_on_element(self.login_option_link_text)
        return LoginPage(self.driver)

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def select_register_option(self):
        self.click_on_element(self.register_option_link_text)
        return RegisterPage(self.driver)

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()
