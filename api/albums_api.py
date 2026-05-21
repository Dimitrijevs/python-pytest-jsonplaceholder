from api.base_client import BaseClient

class AlbumsAPI(BaseClient):

    def get_all_albums(self):
        return self.get("/albums")

    def get_album(self, album_id: int):
        return self.get(f"/albums/{album_id}")

    def create_album(self, data: dict):
        return self.post("/albums", data=data)

    def put_album(self, album_id: int, data: dict):
        return self.put(f"/albums/{album_id}", data=data)

    def patch_album(self, album_id: int, data: dict):
        return self.patch(f"/albums/{album_id}", data=data)

    def delete_album(self, album_id: int):
        return self.delete(f"/albums/{album_id}")

    def get_album_photos(self, album_id: int):
        return self.get(f"/albums/{album_id}/photos")