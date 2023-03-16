from api_client import ApiClient


class ReqresIoApi(ApiClient):

    BASE_URL = 'https://reqres.in/api/users/'
    LIST_URL = 'https://reqres.in/api/unknown/'
    REGISTER_URL = 'https://reqres.in/api/register/'
    LOGIN_URL = 'https://reqres.in/api/login/'

    @classmethod
    def get_users(cls, params: dict = None):
        return ApiClient.get_request(url=cls.BASE_URL, params=params)

    @classmethod
    def create_user(cls, json: dict):
        return ApiClient.post_request(url=cls.BASE_URL, json=json)

    @classmethod
    def update_user(cls, json: dict):
        return ApiClient.put_request(url=cls.BASE_URL, json=json)

    @classmethod
    def delete_user(cls, user_id):
        return ApiClient.delete_request(url=f"{cls.BASE_URL}{user_id}")

    @classmethod
    def update_part_user(cls, json: dict):
        return ApiClient.patch_request(url=cls.BASE_URL, json=json)

    @classmethod
    def get_resource(cls, resource_id):
        return ApiClient.get_request(url=f"{cls.LIST_URL}{resource_id}")

    @classmethod
    def get_list_resource(cls, params: dict = None):
        return ApiClient.get_request(url=cls.LIST_URL, params=params)

    @classmethod
    def register_user(cls, json: dict):
        return ApiClient.post_request(url=cls.REGISTER_URL, json=json)

    @classmethod
    def login_user(cls, json: dict):
        return ApiClient.post_request(url=cls.LOGIN_URL, json=json)



