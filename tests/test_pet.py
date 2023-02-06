
from api import Pets

pt = Pets()


def test_get_token():
    status = pt.get_token()[1]
    assert status == 200


def test_post_registered():
    status = pt.post_registered()[0]
    my_id = pt.post_registered()[1]
    assert my_id
    assert status == 200


def test_get_registered_and_delete():
    status = pt.get_registered_and_delete()[0]
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    amount = pt.get_list_users()[1]
    assert status == 200
    assert amount


def test_post_pet():
    status = pt.post_pet()[1]
    pet_id = pt.post_pet()[0]
    assert status == 200
    assert pet_id


def test_post_pet_photo():
    status = pt.post_pet_photo()
    assert status == 200


def test_post_pets_list():
    status = pt.get_token()[1]
    total = pt.post_pets_list()
    assert status == 200
    assert total


def test_delete_pet():
    status = pt.get_token()[1]
    assert status == 200


def test_update_pet():
    status = pt.patch_update_pet()
    assert status == 200
