import pytest
import requests
import string
import random
from reqres_api import ReqresIoApi
from user_fixture import user_setup
from user_fixture import user_setup_update
from user_fixture import user_setup_part_update
from user_fixture import user_id_setup
from user_fixture import user_fixture
from user_fixture import user_login_setup
from user_fixture import user_fail_login_setup


class TestApi(ReqresIoApi):

    @pytest.mark.API
    def test_get_list_users(self):
        params = {
            "page": 2
        }
        response = ReqresIoApi.get_users(params)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['total'] == 12

    @pytest.mark.API
    def test_get_user(self, user_id_setup):
        """Получаем юзера, id берем из фикстуры user_id_setup"""
        response = ReqresIoApi.get_users(user_id_setup)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body["data"]["id"] == user_id_setup["id"]
        assert response_body["support"]

    @pytest.mark.parametrize("parameters", [
        '23',
        pytest.param('2', marks=pytest.mark.xfail)])
    def test_get_wrong_user(self, parameters):
        """Проверка GET SINGLE USER NOT FOUND, Id=23 не существует, должен вернуть 404
        Для Id=2 вернет 200 => xfail"""
        params = {
            "id": parameters
        }
        response = ReqresIoApi.get_users(params)
        assert response.status_code == 404

    def test_list_resource(self):
        response = ReqresIoApi.get_list_resource()
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['page'] == 1
        assert response_body["per_page"] == 6
        assert response_body["total"] == 12

    def test_get_single_resource(self):
        response = ReqresIoApi.get_resource(resource_id=2)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['data']['name'] == "fuchsia rose"

    @pytest.mark.API
    def test_create_user(self, user_setup):
        """Создаем юзера, параметры берем из фикстуры user_setup"""
        response = ReqresIoApi.create_user(user_setup)
        assert response.status_code == 201
        response_body = response.json()
        assert response_body["name"] == user_setup["name"]
        assert response_body["job"] == user_setup["job"]
        assert response_body["id"]
        assert response_body["createdAt"]

    @pytest.mark.API
    def test_update_user(self, user_setup_update):
        """Обновляем юзера, параметры берем из фикстуры user_setup_update"""
        response = ReqresIoApi.update_user(user_setup_update)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body["updatedAt"]

    @pytest.mark.API
    def test_update_part_user(self, user_setup_part_update):
        """Частично обновляем юзера, параметры берем из фикстуры user_setup_part_update"""
        response = ReqresIoApi.update_user(user_setup_part_update)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body["updatedAt"]

    @pytest.mark.API
    def test_delete_user(self):
        response = ReqresIoApi.delete_user(user_id=2)
        assert response.status_code == 204

    @pytest.mark.API
    def test_register_user(self):
        json = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = ReqresIoApi.register_user(json)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['id'] == 4

    @pytest.mark.API
    def test_fail_register_user(self):
        json = {
            "email": "sydney@fife"
        }
        response = ReqresIoApi.register_user(json)
        assert response.status_code == 400
        response_body = response.json()
        assert response_body['error'] == "Missing password"

    @pytest.mark.API
    def test_login_user(self):
        json = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = ReqresIoApi.login_user(json)
        assert response.status_code == 200
        response_body = response.json()
        assert response_body['token'] == "QpwL5tke4Pnpja7X4"

    @pytest.mark.API
    def test_fail_login_user(self):
        json = {
            "email": "peter@klaven"
        }
        response = ReqresIoApi.login_user(json)
        assert response.status_code == 400
        response_body = response.json()
        assert response_body['error'] == "Missing password"

    @pytest.mark.parametrize("parameters", [
        '3',
        pytest.param('0', marks=pytest.mark.xfail)
    ])
    @pytest.mark.API
    def test_get_delay(self, parameters):
        """Отправляем запрос с задержкой, response.elapsed.total_seconds() - время ответа
        для выставленной задержки в 0s xfail"""
        params = {
            "delay": parameters
        }
        response = ReqresIoApi.get_users(params)
        assert response.status_code == 200
        assert float(response.elapsed.total_seconds()) > 3
