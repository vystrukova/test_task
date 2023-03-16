from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import BasePageLocators
import random


class BasePage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser
        self.base_locators = BasePageLocators

    def return_url(self):
        return self.browser.current_url

    def click(self, locator, timeout=2, retries=2):
        """Кликает на элемент"""
        for i in range(retries):
            if i == retries - 1:
                raise TimeoutException
            try:
                WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
                WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
                break
            except TimeoutException:
                pass

    def click_when_loaded(self, locator, timeout_for_click=5, timeout_for_wait=3,
                          retries_spinner=2, retries_no_spinner=4):
        """Кликает на выбранный элемент после того, как со страницы исчезнет спиннер загрузки."""
        if self.page_is_loaded(timeout_for_wait, retries_spinner, retries_no_spinner):
            WebDriverWait(self.browser, timeout_for_click).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout_for_click).until(EC.element_to_be_clickable(locator)).click()
        else:
            raise TimeoutException

    def page_is_loaded(self, timeout, retries_to_appear, retries_to_disappear):
        """Ждет завершения загрузки страницы, отслеживая появление и исчезновение со страницы спиннера загрузки."""
        for i in range(retries_to_appear):
            try:
                WebDriverWait(self.browser, timeout).until(
                    EC.visibility_of_element_located(self.base_locators.SPINNER))
                for j in range(retries_to_disappear):
                    try:
                        WebDriverWait(self.browser, timeout).until(
                            EC.invisibility_of_element_located(self.base_locators.SPINNER))
                        return True
                    except:
                        if j == retries_to_disappear - 1:
                            return False
                        pass
            except:
                if i == retries_to_appear - 1:
                    return True
                pass

    def get_attribute_value(self, locator, attribute_name, timeout=2):
        """Возвращает значение выбранного атрибута у найденного элемента страницы."""
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute_name)

    def is_visible(self, locator, timeout):
        """Проверяет что элемент visible"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_text(self, locator, timeout):
        """Берет текст из элемента"""
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.text
