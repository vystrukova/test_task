from selenium.webdriver import Chrome

from locators import LoginPageLocators
from base_page import BasePage
import info


class LoginPage(BasePage):
    def __init__(self, browser):
        self.locators = LoginPageLocators
        self.browser: Chrome = browser
        self.url = info.hh_url
        super().__init__(browser)

    def open(self):
        self.browser.get(self.url)
        return self

    def main_page_is_open(self, timeout):
        locator = self.locators.MAIN_SEARCH_INPUT
        return self.wait_for_visible(locator, timeout)

    def click_login_page(self, timeout):
        locator = self.locators.MAIN_LOGIN_BUTTON
        return self.click_visible_element(locator, timeout)

    def click_type_login(self, timeout):
        locator = self.locators.LOGIN_WITH_PASS
        return self.click_visible_element(locator, timeout)

    def login_input_located(self, timeout):
        locator = self.locators.LOGIN_USERNAME
        return self.wait_for_visible(locator, timeout)

    def send_login(self, login_text=info.log):
        locator = self.locators.LOGIN_USERNAME
        if self.login_input_located(timeout=1):
            self.send_keys(locator, login_text)
            return True
        return False

    def pass_input_located(self, timeout):
        locator = self.locators.LOGIN_PASS
        return self.wait_for_visible(locator, timeout)

    def send_pass(self, pass_text=info.pas):
        locator = self.locators.LOGIN_PASS
        if self.pass_input_located(timeout=1):
            self.send_keys(locator, pass_text)
            return True
        return False

    def click_login_button(self, timeout):
        locator = self.locators.LOGIN_BUTTON
        return self.click_visible_element(locator, timeout)

    def my_resumes_located(self, timeout):
        locator = self.locators.LOGIN_MY_RESUMES
        return self.wait_for_visible(locator, timeout)