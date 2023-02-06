import json
import uuid

import requests


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        # self.my_token = None
        self.base_url = 'http://34.141.58.52:8000/'

    def post_registered(self) -> json:
        data = {'email': 'dens@mail.ru', 'password': '1234', 'confirm_password': '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        user_id = res.json()
        user_id = user_id.get('id')
        status = res.status_code
        print(user_id)
        return status, user_id

    def get_token(self) -> json:
        data = {"email": 'dens@mail.ru',
                "password": '1234'}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        user_id = res.json()['id']
        status = res.status_code
        print(my_token)
        print(res.json())
        return my_token, status, user_id

    def delete_user(self) -> json:
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        user_id = Pets().get_token()[2]
        res = requests.delete(self.base_url + f'users/{user_id}', headers=headers)
        status = res.status_code
        print(res.json())
        return status


Pets().post_registered()
Pets().get_token()
Pets().delete_user()
