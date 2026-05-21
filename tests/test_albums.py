import pytest

from models.album import Album
from models.album_photo import AlbumPhoto
from tests.base_test import BaseTest
from utils.constants import ALBUM_IDS, ALBUM_IDS_NON_EXISTING


@pytest.mark.smoke
@pytest.mark.full
@pytest.mark.album
class TestAlbum(BaseTest):

    def test_get_all_albums(self, albums_api):
        response = albums_api.get_all_albums()

        Album.assert_status_code(response, 200)

        albums = [Album(**a) for a in response.json()]
        for album in albums:
            album.assert_valid()

    @pytest.mark.parametrize("album_id", ALBUM_IDS)
    def test_get_album_by_id(self, albums_api, album_id):
        response = albums_api.get_album(album_id)

        Album.assert_status_code(response, 200)

        album = Album(**response.json())
        album.assert_valid(expected_id=album_id)

    def test_create_album(self, albums_api, album_payload):
        response = albums_api.create_album(album_payload)

        Album.assert_status_code(response, 201)

        album = Album(**response.json())
        album.assert_valid(
            expected_title=album_payload["title"],
            expected_user_id=album_payload["userId"],
        )

    def test_put_album(self, albums_api, album_payload):
        response = albums_api.put_album(1, album_payload)

        Album.assert_status_code(response, 200)

        album = Album(**response.json())
        album.assert_valid(
            expected_title=album_payload["title"],
            expected_user_id=album_payload["userId"],
        )

    def test_patch_album(self, albums_api, album_title):
        response = albums_api.patch_album(1, {"title": album_title})

        Album.assert_status_code(response, 200)

        album = Album(**response.json())
        album.assert_valid(
            expected_id=1,
            expected_title=album_title,
            expected_user_id=album.userId
        )

    def test_delete_album(self, albums_api):
        response = albums_api.delete_album(1)

        Album.assert_status_code(response, 200)
        Album.assert_empty_body(response)

    @pytest.mark.parametrize("album_id", ALBUM_IDS)
    def test_get_album_photos(self, albums_api, album_id):
        response = albums_api.get_album_photos(album_id)

        Album.assert_status_code(response, 200)

        photos = [AlbumPhoto(**p) for p in response.json()]
        for photo in photos:
            photo.assert_valid(expected_album_id=album_id)


@pytest.mark.full
@pytest.mark.album
@pytest.mark.negative
class TestAlbumNegative(BaseTest):

    @pytest.mark.parametrize("album_id", ALBUM_IDS_NON_EXISTING)
    def test_get_album_by_non_existing_album(self, albums_api, album_id):
        response = albums_api.get_album(album_id)

        Album.assert_status_code(response, 404)
        Album.assert_empty_body(response)

    def test_create_album_missing_title(self, albums_api, album_user_id):
        payload = {"userId": album_user_id}
        response = albums_api.create_album(payload)

        Album.assert_status_code(response, 201)

        data = response.json()
        assert data["userId"] == album_user_id
        assert "title" not in data

    def test_create_album_empty_payload(self, albums_api):
        response = albums_api.create_album({})

        Album.assert_status_code(response, 201)
        assert response.json() == {"id": 101}

    @pytest.mark.parametrize("album_id", ALBUM_IDS_NON_EXISTING)
    def test_put_non_existing_album(self, albums_api, album_payload, album_id):
        response = albums_api.put_album(album_id, album_payload)

        Album.assert_status_code(response, 500)

    @pytest.mark.parametrize("album_id", ALBUM_IDS_NON_EXISTING)
    def test_delete_non_existing_album(self, albums_api, album_id):
        response = albums_api.delete_album(album_id)

        Album.assert_status_code(response, 200)
        Album.assert_empty_body(response)

    @pytest.mark.parametrize("album_id", ALBUM_IDS_NON_EXISTING)
    def test_get_photos_non_existing_album(self, albums_api, album_id):
        response = albums_api.get_album_photos(album_id)

        Album.assert_status_code(response, 200)
        Album.assert_empty_list(response)