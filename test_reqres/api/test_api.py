import allure
import pytest
from reqres_api import ReqresIoApi


class TestApi(ReqresIoApi):

    @pytest.mark.API
    def test_get_list_users(self):
        params = {
            "page": 2
        }
        response = ReqresIoApi.get_users(params)
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        response_body = response.json()
        with allure.step("Проверяем total == 12"):
            assert response_body['total'] == 12

    @pytest.mark.API
    def test_get_user(self, user_id_setup):
        """Получаем юзера, id берем из фикстуры user_id_setup"""
        response = ReqresIoApi.get_users(user_id_setup)
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        response_body = response.json()
        with allure.step("Проверяем на соответствие id"):
            assert response_body["data"]["id"] == user_id_setup["id"]
        with allure.step("Проверяем ответ"):
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
        with allure.step("Проверяем ответ == 404"):
            assert response.status_code == 404

    @pytest.mark.API
    def test_list_resource(self):
        response = ReqresIoApi.get_list_resource()
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        response_body = response.json()
        with allure.step("Проверяем page == 1"):
            assert response_body['page'] == 1
        with allure.step("Проверяем per_page == 6"):
            assert response_body["per_page"] == 6
        with allure.step("Проверяем total == 12"):
            assert response_body["total"] == 12

    @pytest.mark.API
    def test_get_single_resource(self):
        response = ReqresIoApi.get_resource(resource_id=2)
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        response_body = response.json()
        with allure.step("Проверяем data и name"):
            assert response_body['data']['name'] == "fuchsia rose"

    @pytest.mark.API
    def test_create_user(self, user_setup):
        """Создаем юзера, параметры берем из фикстуры user_setup"""
        response = ReqresIoApi.create_user(user_setup)
        with allure.step("Проверяем ответ == 201"):
            assert response.status_code == 201
        response_body = response.json()
        with allure.step("Проверяем name"):
            assert response_body["name"] == user_setup["name"]
        with allure.step("Проверяем job"):
            assert response_body["job"] == user_setup["job"]
        with allure.step("Проверяем id"):
            assert response_body["id"]
        with allure.step("Проверяем createdAt"):
            assert response_body["createdAt"]

    @pytest.mark.API
    def test_update_user(self, user_setup_update):
        """Обновляем юзера, параметры берем из фикстуры user_setup_update"""
        response = ReqresIoApi.update_user(user_setup_update)
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        response_body = response.json()
        with allure.step("Проверяем updatedAt"):
            assert response_body["updatedAt"]

    @pytest.mark.API
    def test_update_part_user(self, user_setup_part_update):
        """Частично обновляем юзера, параметры берем из фикстуры user_setup_part_update"""
        response = ReqresIoApi.update_user(user_setup_part_update)
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        response_body = response.json()
        with allure.step("Проверяем updatedAt"):
            assert response_body["updatedAt"]

    @pytest.mark.API
    def test_delete_user(self):
        response = ReqresIoApi.delete_user(user_id=2)
        with allure.step("Проверяем ответ == 204"):
            assert response.status_code == 204

    @pytest.mark.API
    def test_register_user(self):
        json = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = ReqresIoApi.register_user(json)
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        response_body = response.json()
        with allure.step("Проверяем id == 4"):
            assert response_body['id'] == 4

    @pytest.mark.API
    def test_fail_register_user(self):
        json = {
            "email": "sydney@fife"
        }
        response = ReqresIoApi.register_user(json)
        with allure.step("Проверяем ответ == 400"):
            assert response.status_code == 400
        response_body = response.json()
        with allure.step("Проверяем error == Missing password"):
            assert response_body['error'] == "Missing password"

    @pytest.mark.API
    def test_login_user(self):
        json = {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
        response = ReqresIoApi.login_user(json)
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        response_body = response.json()
        with allure.step("Проверяем токен"):
            assert response_body['token'] == "QpwL5tke4Pnpja7X4"

    @pytest.mark.API
    def test_fail_login_user(self):
        json = {
            "email": "peter@klaven"
        }
        response = ReqresIoApi.login_user(json)
        with allure.step("Проверяем ответ == 400"):
            assert response.status_code == 400
        response_body = response.json()
        with allure.step("Проверяем error == Missing password"):
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
        with allure.step("Проверяем ответ == 200"):
            assert response.status_code == 200
        with allure.step("Проверяем что время ответа больше 3х секунд"):
            assert float(response.elapsed.total_seconds()) > 3
