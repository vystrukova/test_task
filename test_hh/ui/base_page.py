import time

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators import BasePageLocators


class BasePage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser
        self.base_locators = BasePageLocators

    def return_url(self):
        return self.browser.current_url

    def click(self, locator, timeout=2, retries=2):
        """
        Кликает на элемент
        """
        for i in range(retries):
            if i == retries - 1:
                raise TimeoutException
            try:
                WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
                WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
                break
            except TimeoutException:
                pass

    def click_visible_element(self, locator, timeout):
        """
        Кликает элемент по локатору
        Возвращает True если успешно кликает
        """
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                self.browser.find_element(*locator).click()
                return True
            time.sleep(0.5)
        return False

    def get_attribute_value(self, locator, attribute_name, timeout=2):
        """
        Возвращает значение выбранного атрибута у найденного элемента страницы.
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute(attribute_name)

    def is_visible(self, locator, timeout):
        """
        Проверяет что элемент visible
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def get_text(self, locator, timeout):
        """
        Берет текст из элемента
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_src(self, locator, timeout):
        """
        Берет src из элемента
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute("src")

    def get_href(self, locator, timeout):
        """
        Берет href из элемента
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute("href")

    def get_input_value(self, locator, timeout):
        """
        Берет значение из поля ввода
        """
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        return element.get_attribute("value")

    def send_keys(self, locator, text, timeout=2):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def send_enter(self, locator, timeout=2):
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        element = WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))
        element.send_keys(Keys.ENTER)

    def switch_tab(self, index):
        """
        Меняет вкладку в браузере по индексу
        """
        handles = self.browser.window_handles
        if index >= len(handles):
            raise Exception(f"Invalid tab index {index}")
        self.browser.switch_to.window(handles[index])

    def wait_for_clickable(self, locator, timeout):
        try:
            element = WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator))
            return element
        except:
            return None

    def wait_for_visible(self, locator, timeout):
        for _ in range(timeout):
            if self.is_visible(locator, timeout):
                return True
            time.sleep(0.5)
        return False