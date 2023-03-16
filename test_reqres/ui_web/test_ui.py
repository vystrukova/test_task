import pytest
from main_page import MainPage


class TestReqresin:

    @pytest.mark.UI
    def test_open(self, browser):
        """Проверяем что открывается страница MainPage"""
        page = MainPage(browser=browser).open()
        assert page.page_is_open(timeout=1) is True

    @pytest.mark.UI
    def test_request_located(self, browser):
        """Проверяем что на странице есть список запросов"""
        page = MainPage(browser=browser).open()
        assert page.requests_is_located(timeout=1) is True

    @pytest.mark.parametrize("code_response", [
        '200',
        pytest.param('404', marks=pytest.mark.xfail)])
    @pytest.mark.UI
    def test_response_located(self, browser, code_response):
        """Проверяем код ответа у GET запроса SINGLE USER"""
        page = MainPage(browser=browser).open()
        page.click_single_user(timeout=1)
        assert page.get_response_code_value(timeout=1) == code_response