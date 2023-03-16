import pytest
from ui_web.main_page import MainPage
from test_reqres.api.reqres_api import ReqresIoApi
from test_reqres.api.user_fixture import user_fixture


@pytest.mark.skip
class TestResponse(ReqresIoApi):

    @pytest.mark.UI
    def test_response_located(self, browser):
        page = MainPage(browser=browser).open()
        page.click_single_user(timeout=1)
        params = {
            "id": 2
        }
        response = ReqresIoApi.get_users(params)
        assert page.get_response_code_value(timeout=3) == str(response.status_code)
