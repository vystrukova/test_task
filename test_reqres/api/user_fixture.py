import pytest
import string
import random
from reqres_api import ReqresIoApi


def generate_user() -> dict:
    user_info = {
        "name": "".join(random.choice(string.ascii_letters) for _ in range(10)),
        "job": "".join(random.choice(string.ascii_letters) for _ in range(16)),
    }
    return user_info


def create_id_user() -> dict:
    user_id = {
        "id": "".join(str(random.randint(1, 12)))
    }
    return user_id


def generate_login_user() -> dict:
    login_pass = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    return login_pass


def generate_fail_login_user() -> dict:
    login = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    return login


def generate_register_user() -> dict:
    user_register = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    return user_register


def generate_failed_register_user() -> dict:
    user_failed_register = {
        "email": "sydney@fife"
    }
    return user_failed_register


@pytest.fixture(scope="function", autouse=False)
def user_fail_login_setup() -> dict:
    """Фикстура для авторизации пользователя"""
    payload = generate_failed_register_user()
    response = ReqresIoApi.login_user(payload)
    payload["error"] = response.json()["error"]
    yield payload


@pytest.fixture(scope="function", autouse=False)
def user_login_setup() -> dict:
    """Фикстура для авторизации пользователя"""
    payload = generate_login_user()
    response = ReqresIoApi.login_user(payload)
    payload["token"] = response.json()["token"]
    yield payload


@pytest.fixture(scope="function", autouse=False)
def user_id_setup() -> dict:
    """Фикстура для генерации id"""
    payload = create_id_user()
    response = ReqresIoApi.get_users(payload)
    payload["id"] = response.json()["data"]["id"]
    yield payload


@pytest.fixture(scope="function", autouse=False)
def user_setup() -> dict:
    """Фикстура для создания пользователя"""
    payload = generate_user()
    response = ReqresIoApi.create_user(payload)
    payload["id"] = response.json()["id"]
    yield payload


@pytest.fixture(scope="function", autouse=False)
def user_setup_update() -> dict:
    """Фикстура для полного обновления пользователя"""
    payload = generate_user()
    response = ReqresIoApi.update_user(payload)
    payload["updatedAt"] = response.json()["updatedAt"]
    yield payload


@pytest.fixture(scope="function", autouse=False)
def user_setup_part_update() -> dict:
    """Фикстура для частичного обновления пользователя"""
    payload = generate_user()
    response = ReqresIoApi.update_part_user(payload)
    payload["name"] = response.json()["name"]
    yield payload


@pytest.fixture(scope="function", autouse=False)
def user_teardown() -> dict:
    """Фикстура для удаления пользователя после выполнения теста"""
    payload = generate_user()
    yield payload
    params = {
        "name": payload["name"]
    }
    response = ReqresIoApi.get_users(params)
    response_body = response.json()
    user_id = response_body[0].get("id")
    if user_id is not None:
        ReqresIoApi.delete_user(user_id=user_id)


@pytest.fixture(scope="function", autouse=False)
def user_fixture() -> dict:
    """Фикстура для создания пользователя перед тестом и удаления пользователя после теста"""
    payload = generate_user()
    response = ReqresIoApi.create_user(payload)
    payload["id"] = response.json()["id"]
    yield payload
    ReqresIoApi.delete_user(user_id=payload["id"])


@pytest.fixture(scope="function", autouse=False)
def user_register_setup() -> dict:
    """Фикстура для генерации пользователя перед авторизацией"""
    payload = generate_register_user()
    response = ReqresIoApi.register_user(payload)
    payload["id"] = response.json()["id"]
    yield payload
