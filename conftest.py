import pytest

from api.posts_api import PostsAPI
from utils.post_data_generator import generate_post_payload, generate_post_title, generate_post_body, generate_post_user_id


@pytest.fixture(scope="session")
def posts_api():
    return PostsAPI()

@pytest.fixture
def post_payload():
    return generate_post_payload()

@pytest.fixture
def post_title():
    return generate_post_title()

@pytest.fixture
def post_body():
    return generate_post_body()

@pytest.fixture
def post_user_id():
    return generate_post_user_id()
