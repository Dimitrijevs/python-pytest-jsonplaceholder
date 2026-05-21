import pytest

from models.album import Album
from models.post import Post
from models.user import User
from models.todo import Todo
from tests.base_test import BaseTest
from utils.constants import USER_IDS, USER_IDS_NON_EXISTING


@pytest.mark.full
@pytest.mark.smoke
@pytest.mark.user
class TestUsers(BaseTest):

    def test_get_all_users(self, users_api):
        response = users_api.get_all_users()

        User.assert_status_code(response, 200)

        users = [User(**u) for u in response.json()]
        for user in users:
            user.assert_valid()

    @pytest.mark.parametrize("user_id", USER_IDS)
    def test_get_user_by_id(self, users_api, user_id):
        response = users_api.get_user(user_id)

        User.assert_status_code(response, 200)

        user = User(**response.json())
        user.assert_valid(expected_id=user_id)

    def test_create_user(self, users_api, user_payload):
        response = users_api.create_user(user_payload)

        User.assert_status_code(response, 201)

        user = User(**response.json())
        user.assert_valid(
            expected_name=user_payload["name"],
            expected_username=user_payload["username"],
            expected_email=user_payload["email"]
        )

    def test_put_user(self, users_api, user_payload):
        response = users_api.put_user(1, user_payload)

        User.assert_status_code(response, 200)

        user = User(**response.json())
        user.assert_valid(
            expected_name=user_payload["name"],
            expected_username=user_payload["username"],
            expected_email=user_payload["email"]
        )

    def test_patch_user(self, users_api, user_name):
        response = users_api.patch_user(1, {"name": user_name})

        User.assert_status_code(response, 200)

        user = User(**response.json())
        user.assert_valid(
            expected_id=1,
            expected_name=user_name
        )

    def test_delete_user(self, users_api):
        response = users_api.delete_user(1)

        User.assert_status_code(response, 200)
        User.assert_empty_body(response)

    @pytest.mark.parametrize("user_id", USER_IDS)
    def test_get_user_albums(self, users_api, user_id):
        response = users_api.get_user_albums(user_id)

        User.assert_status_code(response, 200)

        albums = [Album(**a) for a in response.json()]
        for album in albums:
            assert album.userId == user_id

    @pytest.mark.parametrize("user_id", USER_IDS)
    def test_get_user_posts(self, users_api, user_id):
        response = users_api.get_user_posts(user_id)

        User.assert_status_code(response, 200)

        posts = [Post(**p) for p in response.json()]
        for post in posts:
            assert post.userId == user_id

    @pytest.mark.parametrize("user_id", USER_IDS)
    def test_get_user_todos(self, users_api, user_id):
        response = users_api.get_user_todos(user_id)

        User.assert_status_code(response, 200)

        todos = [Todo(**t) for t in response.json()]
        for todo in todos:
            assert todo.userId == user_id


@pytest.mark.full
@pytest.mark.user
@pytest.mark.negative
class TestUserNegative(BaseTest):

    @pytest.mark.parametrize("user_id", USER_IDS_NON_EXISTING)
    def test_get_user_by_non_existing_id(self, users_api, user_id):
        response = users_api.get_user(user_id)

        User.assert_status_code(response, 404)
        User.assert_empty_body(response)

    def test_create_user_missing_name(self, users_api, user_payload):
        user_payload.pop("name")
        response = users_api.create_user(user_payload)

        User.assert_status_code(response, 201)

        data = response.json()
        assert "name" not in data

    def test_create_user_empty_payload(self, users_api):
        response = users_api.create_user({})

        User.assert_status_code(response, 201)
        assert response.json() == {"id": 11}

    @pytest.mark.parametrize("user_id", USER_IDS_NON_EXISTING)
    def test_put_non_existing_user(self, users_api, user_payload, user_id):
        response = users_api.put_user(user_id, user_payload)

        User.assert_status_code(response, 500)

    @pytest.mark.parametrize("user_id", USER_IDS_NON_EXISTING)
    def test_delete_non_existing_user(self, users_api, user_id):
        response = users_api.delete_user(user_id)

        User.assert_status_code(response, 200)
        User.assert_empty_body(response)

    @pytest.mark.parametrize("user_id", USER_IDS_NON_EXISTING)
    def test_get_albums_non_existing_user(self, users_api, user_id):
        response = users_api.get_user_albums(user_id)

        User.assert_status_code(response, 200)
        User.assert_empty_list(response)

    @pytest.mark.parametrize("user_id", USER_IDS_NON_EXISTING)
    def test_get_posts_non_existing_user(self, users_api, user_id):
        response = users_api.get_user_posts(user_id)

        User.assert_status_code(response, 200)
        User.assert_empty_list(response)

    @pytest.mark.parametrize("user_id", USER_IDS_NON_EXISTING)
    def test_get_todos_non_existing_user(self, users_api, user_id):
        response = users_api.get_user_todos(user_id)

        User.assert_status_code(response, 200)
        User.assert_empty_list(response)