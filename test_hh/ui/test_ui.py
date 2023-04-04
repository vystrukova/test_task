import allure
import pytest

from login_page import LoginPage


class TestHh:

    @pytest.mark.UI
    def test_open(self, browser):
        page = LoginPage(browser=browser).open()
        with allure.step("Проверяем что открывается hh.ru"):
            assert page.main_page_is_open(timeout=1) is True

    @pytest.mark.UI
    def test_login(self,browser):
        page = LoginPage(browser=browser).open()
        page.click_login_page(timeout=1)
        page.click_type_login(timeout=1)
        with allure.step("Проверяем что есть инпут для логина"):
            assert page.login_input_located(timeout=1) is True
        page.send_login()
        with allure.step("Проверяем что есть инпут для пароля"):
            assert page.pass_input_located(timeout=1) is True
        page.send_pass()
        page.click_login_button(timeout=1)
        with allure.step("Проверяем что появились Мои резюме"):
            assert page.my_resumes_located(timeout=1)