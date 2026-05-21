import pytest

from models.user import User
from models.album import Album
from models.post import Post
from tests.base_test import BaseTest


@pytest.mark.full
@pytest.mark.smoke
@pytest.mark.user
class TestUsers(BaseTest):

    def test_get_all_users(self, users_api):
        response = users_api.get_all_users()

        assert response.status_code == 200

        users = [User(**u) for u in response.json()]
        for user in users:
            user.assert_valid()

    def test_get_user_by_id(self, users_api):
        response = users_api.get_user(1)

        assert response.status_code == 200

        user = User(**response.json())
        user.assert_valid(expected_id=1)

    def test_create_user(self, users_api, user_payload):
        response = users_api.create_user(user_payload)

        assert response.status_code == 201

        user = User(**response.json())

        user.assert_valid(
            expected_name=user_payload["name"],
            expected_username=user_payload["username"],
            expected_email=user_payload["email"]
        )

    def test_put_user(self, users_api, user_payload):
        response = users_api.put_user(1, user_payload)

        assert response.status_code == 200

        user = User(**response.json())
        user.assert_valid(
            expected_name=user_payload["name"],
            expected_username=user_payload["username"],
            expected_email=user_payload["email"]
        )

    def test_patch_user(self, users_api, user_name):
        response = users_api.patch_user(1, {"name": user_name})

        assert response.status_code == 200

        user = User(**response.json())
        user.assert_valid(
            expected_id=1,
            expected_name=user_name
        )

    def test_delete_user(self, users_api):
        response = users_api.delete_user(1)

        assert response.status_code == 200
        assert response.json() == {}

    def test_get_user_albums(self, users_api):
        response = users_api.get_user_albums(1)

        assert response.status_code == 200

        albums = [Album(**a) for a in response.json()]
        for album in albums:
            assert album.userId == 1

    def test_get_user_posts(self, users_api):
        response = users_api.get_user_posts(1)

        assert response.status_code == 200

        posts = [Post(**p) for p in response.json()]
        for post in posts:
            assert post.userId == 1


@pytest.mark.full
@pytest.mark.user
class TestUserNegative(BaseTest):

    def test_get_user_by_non_existing_id(self, users_api):
        response = users_api.get_user(9999)

        assert response.status_code == 404
        assert response.json() == {}

    def test_create_user_missing_name(self, users_api, user_payload):
        user_payload.pop("name")
        response = users_api.create_user(user_payload)

        assert response.status_code == 201

        data = response.json()
        assert "name" not in data

    def test_create_user_empty_payload(self, users_api):
        response = users_api.create_user({})

        assert response.status_code == 201
        assert response.json() == {"id": 11}

    def test_put_non_existing_user(self, users_api, user_payload):
        response = users_api.put_user(9999, user_payload)

        assert response.status_code == 500

    def test_delete_non_existing_user(self, users_api):
        response = users_api.delete_user(9999)

        assert response.status_code == 200
        assert response.json() == {}

    def test_get_albums_non_existing_user(self, users_api):
        response = users_api.get_user_albums(9999)

        assert response.status_code == 200
        assert response.json() == []

    def test_get_posts_non_existing_user(self, users_api):
        response = users_api.get_user_posts(9999)

        assert response.status_code == 200
        assert response.json() == []