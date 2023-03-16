import requests


class ApiClient:

    @classmethod
    def post_request(cls, url, data=None, json=None, **kwargs):
        return requests.post(url, data, json, **kwargs)

    @classmethod
    def get_request(cls, url, params=None, **kwargs):
        return requests.get(url, params, **kwargs)

    @classmethod
    def put_request(cls, url, data=None, **kwargs):
        return requests.put(url, data, **kwargs)

    @classmethod
    def delete_request(cls, url, **kwargs):
        return requests.delete(url, **kwargs)

    @classmethod
    def patch_request(cls, url, data=None, **kwargs):
        return requests.patch(url, data, **kwargs)
