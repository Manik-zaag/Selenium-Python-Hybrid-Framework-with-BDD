import argparse

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from utilities import ConfigReader


def parse_args():
    """
    Pass command-line options through jenkins
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--browser', type=str, required=True, help="Specify the browser to use (chrome, firefox, edge)")
    return parser.parse_args()


def before_scenario(context, driver):
    args = parse_args()
    browser = args.browser

    # browser = ConfigReader.read_configuration("basic info", "browser")
    headless = ConfigReader.read_configuration("basic info", "headless") == "true"
    maximized = ConfigReader.read_configuration("basic info", "maximized") == "true"  # Read maximized setting
    fullscreen = ConfigReader.read_configuration("basic info", "fullscreen") == "true"

    if browser.lower().__eq__("chrome"):
        chrome_options = ChromeOptions()
        # Disable automation info bar by setting preferences
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        # Disable Web Push Notification
        chrome_options.add_argument("--disable-notifications")  # Disable notifications
        if headless:
            chrome_options.add_argument("--headless")
        if maximized:
            chrome_options.add_argument("--start-maximized")  # Maximize the window
        if fullscreen:
            chrome_options.add_argument("--start-fullscreen")  # Start in full-screen mode
        context.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    elif browser.lower().__eq__("firefox"):
        firefox_options = FirefoxOptions()
        firefox_options.set_preference("dom.push.enabled", False) # Disable web push notification
        if headless:
            firefox_options.add_argument("--headless")
        if maximized:
            firefox_options.add_argument("--start-maximized")  # Maximize the window
        context.driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)
        if fullscreen:
            context.driver.fullscreen_window()  # Use Selenium method to enter full-screen mode
    elif browser.lower().__eq__("edge"):
        edge_options = EdgeOptions()
        # Disable automation info bar by setting preferences
        edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        edge_options.add_experimental_option("useAutomationExtension", False)
        edge_options.add_argument('--disable-blink-features=AutomationControlled')
        # Disable web push notification
        edge_options.add_argument("--disable-notifications")  # Disable notifications
        if headless:
            edge_options.add_argument("--headless")
        if maximized:
            edge_options.add_argument("--start-maximized")  # Maximize the window
        if fullscreen:
            edge_options.add_argument("--start-fullscreen")  # Start in full-screen mode
        context.driver = webdriver.Edge(service=EdgeService(), options=edge_options)
    else:
        print("Provide a valid browser name from this list chrom/firefox/edge")

    # context.driver.maximize_window()
    base_url = ConfigReader.read_configuration("basic info", "url")
    context.driver.get(base_url)
    # driver.implicitly_wait(7)


def after_scenario(context, driver):
    context.driver.quit()


# To take a screenshot only on failure, write the following method (after_step)
def after_step(context, step):
    if step.status == "failed":
        # Access the scenario title
        scenario_title = context.scenario.name if hasattr(context, 'scenario') else 'Scenario_Failed'
        # Attach screenshot to Allure report with scenario title
        allure.attach(context.driver.get_screenshot_as_png()
                      , name=f"Scenario: {scenario_title} failed"
                      , attachment_type=AttachmentType.PNG)


