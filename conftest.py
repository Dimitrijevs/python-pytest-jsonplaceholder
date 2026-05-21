import pytest

from api.posts_api import PostsAPI
from api.albums_api import AlbumsAPI
from api.users_api import UsersAPI

from utils.post_data_generator import generate_post_payload, generate_post_title, generate_post_body, generate_post_user_id
from utils.album_data_generator import generate_album_title, generate_album_user_id, generate_album_payload
from utils.user_data_generator import generate_user_payload, generate_user_name

@pytest.fixture(scope="session")
def posts_api():
    return PostsAPI()

@pytest.fixture(scope="session")
def albums_api():
    return AlbumsAPI()

@pytest.fixture(scope="session")
def users_api():
    return UsersAPI()


# post
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


# album
@pytest.fixture
def album_payload():
    return generate_album_payload()

@pytest.fixture
def album_title():
    return generate_album_title()

@pytest.fixture
def album_user_id():
    return generate_album_user_id()


# user
@pytest.fixture
def user_payload():
    return generate_user_payload()

@pytest.fixture
def user_name():
    return generate_user_name()