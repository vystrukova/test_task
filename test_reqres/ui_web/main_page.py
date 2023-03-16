import time

from selenium.webdriver import Chrome

from locators import MainPageLocators
from base_page import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        self.locators = MainPageLocators
        self.browser: Chrome = browser
        self.url = "https://reqres.in/"
        super().__init__(browser)

    def open(self):
        self.browser.get(self.url)
        return self

    def page_is_open(self, timeout):
        locator = self.locators.LOGO_REQRES
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False

    def page_is_not_open(self, timeout):
        locator = self.locators.LOGO_FAIL_REQRES
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False

    def requests_is_located(self, timeout):
        locator = self.locators.LIST_OF_ALL_REQUESTS
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False

    def requests_not_located(self, timeout):
        locator = self.locators.FAKE_LIST_OF_ALL_REQUESTS
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False

    def get_response_code_value(self, timeout):
        locator = self.locators.RESPONSE_CODE
        for _ in range(timeout):
            if self.get_text(locator, timeout):
                return self.get_text(locator, timeout)
            time.sleep(0.5)
        return False

    def click_register_successful(self, timeout):
        locator = self.locators.REGISTER_SUCCESSFUL
        self.click(locator, timeout)

    def click_single_user(self, timeout):
        locator = self.locators.SINGLE_USER
        self.click(locator, timeout)