import pytest

from models.album import Album
from models.album_photo import AlbumPhoto
from tests.base_test import BaseTest


class TestAlbum(BaseTest):

    @pytest.mark.smoke
    def test_get_all_albums(self, albums_api):
        response = albums_api.get_all_albums()

        assert response.status_code == 200

        albums = [Album(**a) for a in response.json()]
        assert len(albums) == 100

    @pytest.mark.smoke
    def test_get_album_by_id(self, albums_api):
        response = albums_api.get_album(1)

        assert response.status_code == 200

        album = Album(**response.json())
        assert album.id == 1

    @pytest.mark.smoke
    def test_create_album(self, albums_api, album_payload):
        response = albums_api.create_album(album_payload)

        assert response.status_code == 201

        album = Album(**response.json())
        assert album.title == album_payload["title"]
        assert album.userId == album_payload["userId"]

    @pytest.mark.smoke
    def test_put_album(self, albums_api, album_payload):
        response = albums_api.put_album(1, album_payload)

        assert response.status_code == 200

        album = Album(**response.json())
        assert album.title == album_payload["title"]
        assert album.userId == album_payload["userId"]

    @pytest.mark.smoke
    def test_patch_album(self, albums_api, album_title):
        response = albums_api.patch_album(1, {"title": album_title})

        assert response.status_code == 200

        album = Album(**response.json())
        assert album.id == 1
        assert album.title == album_title

    @pytest.mark.smoke
    def test_delete_album(self, albums_api):
        response = albums_api.delete_album(1)

        assert response.status_code == 200

        assert response.json() == {}

    @pytest.mark.smoke
    def test_get_album_photos(self, albums_api):
        response = albums_api.get_album_photos(1)

        assert response.status_code == 200

        photos = [AlbumPhoto(**p) for p in response.json()]
        for photo in photos:
            assert photo.albumId == 1


@pytest.mark.full
class TestAlbumNegative(BaseTest):

    def test_get_non_existing_album(self, albums_api):
        response = albums_api.get_album(999)

        assert response.status_code == 404
        assert response.json() == {}

    def test_create_album_missing_title(self, albums_api, album_user_id):
        payload = {"userId": album_user_id}
        response = albums_api.create_album(payload)

        assert response.status_code == 201

        data = response.json()
        assert data["userId"] == album_user_id
        assert "title" not in data

    def test_create_album_empty_payload(self, albums_api):
        response = albums_api.create_album({})

        assert response.status_code == 201
        assert response.json() == {"id": 101}

    def test_put_non_existing_album(self, albums_api, album_payload):
        response = albums_api.put_album(999, album_payload)

        assert response.status_code == 500

    def test_delete_non_existing_album(self, albums_api):
        response = albums_api.delete_album(999)

        assert response.status_code == 200
        assert response.json() == {}

    def test_get_photos_non_existing_album(self, albums_api):
        response = albums_api.get_album_photos(999)

        assert response.status_code == 200
        assert response.json() == []