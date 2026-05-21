import pytest

from models.post_comment import PostComment
from models.post import Post
from tests.base_test import BaseTest


class TestPosts(BaseTest):

    @pytest.mark.smoke
    def test_get_all_posts(self, posts_api):
        response = posts_api.get_all_posts()

        assert response.status_code == 200

        posts = [Post(**p) for p in response.json()]

        for post in posts:
            post.assert_valid()

    @pytest.mark.smoke
    def test_get_post_by_id(self, posts_api):
        response = posts_api.get_post(1)

        assert response.status_code == 200

        post = Post(**response.json())
        post.assert_valid(expected_id=1)

    @pytest.mark.smoke
    def test_create_post(self, posts_api, post_payload):
        response = posts_api.create_post(post_payload)

        assert response.status_code == 201

        post = Post(**response.json())
        post.assert_valid(
            expected_title=post_payload["title"],
            expected_body=post_payload["body"],
            expected_user_id=post_payload["userId"]
        )

    @pytest.mark.smoke
    def test_put_post(self, posts_api, post_payload):
        response = posts_api.put_post(1, post_payload)

        assert response.status_code == 200

        post = Post(**response.json())
        post.assert_valid(
            expected_title=post_payload["title"],
            expected_body=post_payload["body"],
            expected_user_id=post_payload["userId"]
        )

    @pytest.mark.smoke
    def test_patch_post(self, posts_api, post_title):
        response = posts_api.patch_post(1, {"title": post_title})

        assert response.status_code == 200

        post = Post(**response.json())

        post.assert_valid(
            expected_id=1,
            expected_title = post_title,
            expected_body = post.body,
            expected_user_id = post.userId
        )

    @pytest.mark.smoke
    def test_delete_post(self, posts_api):
        response = posts_api.delete_post(1)

        assert response.status_code == 200

        assert response.json() == {}

    def test_get_post_comments(self, posts_api):
        response = posts_api.get_post_comments(1)

        assert response.status_code == 200

        comments = [PostComment(**c) for c in response.json()]

        for comment in comments:
            assert comment.postId == 1


@pytest.mark.full
class TestPostNegative(BaseTest):

    @pytest.mark.smoke
    def test_get_post_by_non_existing_id(self, posts_api):
        response = posts_api.get_post(999)

        assert response.status_code == 404

        assert response.json() == {}

    def test_create_post_missing_title(self, posts_api, post_body, post_user_id):
        post_payload = {
            "body": post_body,
            "userId": post_user_id
        }
        response = posts_api.create_post(post_payload)

        assert response.status_code == 201

        data = response.json()
        assert data["body"] == post_body
        assert data["userId"] == post_user_id
        assert "title" not in data

    def test_create_post_missing_body(self, posts_api, post_title, post_user_id):
        post_payload = {
            "title": post_title,
            "userId": post_user_id
        }
        response = posts_api.create_post(post_payload)

        assert response.status_code == 201

        data = response.json()
        assert data["title"] == post_title
        assert data["userId"] == post_user_id
        assert "body" not in data

    def test_create_post_empty_payload(self, posts_api):
        response = posts_api.create_post({})

        assert response.status_code == 201

        data = response.json()
        assert data == {"id": 101}

    def test_delete_non_existing_post(self, posts_api):
        response = posts_api.delete_post(999)

        assert response.status_code == 200

        assert response.json() == {}

    def test_put_non_existing_post(self, posts_api, post_payload):
        response = posts_api.put_post(999, post_payload)

        assert response.status_code == 500

    def test_get_comments_non_existing_post(self, posts_api):
        response = posts_api.get_post_comments(999)

        assert response.status_code == 200

        assert response.json() == []