import pytest

from models.post_comment import PostComment
from models.post import Post
from tests.base_test import BaseTest
from utils.constants import POST_IDS, POST_IDS_NON_EXISTING


@pytest.mark.full
@pytest.mark.smoke
@pytest.mark.post
class TestPosts(BaseTest):

    def test_get_all_posts(self, posts_api):
        response = posts_api.get_all_posts()

        Post.assert_status_code(response, 200)

        posts = [Post(**p) for p in response.json()]

        for post in posts:
            post.assert_valid()

    @pytest.mark.parametrize("post_id", POST_IDS)
    def test_get_post_by_id(self, posts_api, post_id):
        response = posts_api.get_post(post_id)

        Post.assert_status_code(response, 200)

        post = Post(**response.json())
        post.assert_valid(expected_id=post_id)

    def test_create_post(self, posts_api, post_payload):
        response = posts_api.create_post(post_payload)

        Post.assert_status_code(response, 201)

        post = Post(**response.json())
        post.assert_valid(
            expected_title=post_payload["title"],
            expected_body=post_payload["body"],
            expected_user_id=post_payload["userId"]
        )

    def test_put_post(self, posts_api, post_payload):
        response = posts_api.put_post(1, post_payload)

        Post.assert_status_code(response, 200)

        post = Post(**response.json())
        post.assert_valid(
            expected_title=post_payload["title"],
            expected_body=post_payload["body"],
            expected_user_id=post_payload["userId"]
        )

    def test_patch_post(self, posts_api, post_title):
        response = posts_api.patch_post(1, {"title": post_title})

        Post.assert_status_code(response, 200)

        post = Post(**response.json())

        post.assert_valid(
            expected_id=1,
            expected_title = post_title,
            expected_body = post.body,
            expected_user_id = post.userId
        )

    def test_delete_post(self, posts_api):
        response = posts_api.delete_post(1)

        Post.assert_status_code(response, 200)
        Post.assert_empty_body(response)

    @pytest.mark.parametrize("post_id", POST_IDS)
    def test_get_post_comments(self, posts_api, post_id):
        response = posts_api.get_post_comments(post_id)

        Post.assert_status_code(response, 200)

        comments = [PostComment(**c) for c in response.json()]
        for comment in comments:
            assert comment.postId == post_id


@pytest.mark.full
@pytest.mark.post
@pytest.mark.negative
class TestPostNegative(BaseTest):

    @pytest.mark.parametrize("post_id", POST_IDS_NON_EXISTING)
    def test_get_post_by_non_existing_id(self, posts_api, post_id):
        response = posts_api.get_post(post_id)

        Post.assert_status_code(response, 404)
        Post.assert_empty_body(response)

    def test_create_post_missing_title(self, posts_api, post_body, post_user_id):
        post_payload = {
            "body": post_body,
            "userId": post_user_id
        }
        response = posts_api.create_post(post_payload)

        Post.assert_status_code(response, 201)

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

        Post.assert_status_code(response, 201)

        data = response.json()
        assert data["title"] == post_title
        assert data["userId"] == post_user_id
        assert "body" not in data

    def test_create_post_empty_payload(self, posts_api):
        response = posts_api.create_post({})

        Post.assert_status_code(response, 201)

        data = response.json()
        assert data == {"id": 101}

    @pytest.mark.parametrize("post_id", POST_IDS_NON_EXISTING)
    def test_delete_non_existing_post(self, posts_api, post_id):
        response = posts_api.delete_post(post_id)

        Post.assert_status_code(response, 200)
        Post.assert_empty_body(response)

    @pytest.mark.parametrize("post_id", POST_IDS_NON_EXISTING)
    def test_put_non_existing_post(self, posts_api, post_payload, post_id):
        response = posts_api.put_post(post_id, post_payload)

        Post.assert_status_code(response, 500)

    @pytest.mark.parametrize("post_id", POST_IDS_NON_EXISTING)
    def test_get_comments_non_existing_post(self, posts_api, post_id):
        response = posts_api.get_post_comments(post_id)

        Post.assert_status_code(response, 200)
        Post.assert_empty_list(response)