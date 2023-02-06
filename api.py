import json
import uuid
import requests
from settings import VALID_EMAIL, VALID_PASSWORD


class Pets:
    """ API библиотека к сайту http://34.141.58.52:8080/#/"""

    def __init__(self):
        # self.my_token = None
        self.base_url = 'http://34.141.58.52:8000/'

    def post_registered(self) -> json:
        """Регистрация нового пользователя, с помощью генератора рандомного email"""
        e = uuid.uuid4().hex
        data = {'email': f'{e}@gmail.com', 'password': '1234', 'confirm_password': '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        user_id = res.json()
        user_id = user_id.get('id')
        status = res.status_code
        return status, user_id

    def get_registered_and_delete(self) -> json:
        """Регистрация нового пользователя и последующее его удаление"""
        e = uuid.uuid4().hex
        data = {"email": f'1234@{e}.ru', "password": '1234', "confirm_password": '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        my_id = res.json().get('id')
        my_token = res.json()['token']
        #     status = res.status_code
        #     print(my_id)
        #     print(my_token)
        #     return status, my_id, my_token
        #
        # def delete_user(self) -> json:
        #     my_id = Pets().get_registered()[1]
        #     my_token = Pets().get_registered()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        params = {'id': my_id}
        res = requests.delete(self.base_url + f'users/{my_id}', headers=headers, params=params)
        status = res.status_code
        return status

    def get_token(self) -> json:
        """Запрос к Swagger сайта для получения уникального токена пользователя по указанным email и password"""
        data = {"email": VALID_EMAIL,
                "password": VALID_PASSWORD}
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        status = res.status_code
        return my_token, status, my_id

    # Pets().get_token()

    def get_list_users(self) -> json:
        """Запрос к Swagger сайта для получения списка пользователей (но получаем свой id)"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        amount = res.json
        return status, amount

    def post_pet(self) -> json:
        """Добавление нового питомца к себе в профиль"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id,
                "name": 'Hitman', "type": 'dog', "age": 5, "owner_id": my_id}
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return pet_id, status

    def delete_pet(self) -> json:
        """Удаление питомца из своего профиля"""
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        pet_id = Pets().post_pet()[0]
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        return status

    def post_pet_photo(self) -> json:
        """Добавление фотографии питомцу по id питомца"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        # pic = open('tests/photo\\pet.jpg', 'rb')
        files = {'pic': ('pic.jpg', open('/Users/DENIS/PycharmProjects/API Tests/tests/photo/pet1.jpg', 'rb'),
                         'image/jpg')}
        res = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        status = res.status_code
        return status

    def post_pets_list(self) -> json:
        """Получение списка питомцев своего профиля"""
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[2]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": my_id}
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        total = res.json
        return status, total

    def patch_update_pet(self) -> json:
        """Обновление информации о питомце по его id"""
        my_token = Pets().get_token()[0]
        pet_id = Pets().post_pet()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": pet_id, "name": 'Hitman2', "type": 'cat', "age": 5}
        res = requests.patch(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status


Pets().get_token()
Pets().get_list_users()
Pets().post_pet()
Pets().post_pet_photo()
Pets().post_pets_list()
Pets().post_registered()
Pets().delete_pet()
Pets().get_registered_and_delete()
Pets().patch_update_pet()
