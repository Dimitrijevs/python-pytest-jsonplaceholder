from typing import Optional
from models.base_api_model import BaseAPIModel

class AlbumPhoto(BaseAPIModel):
    albumId: int
    id: int
    title: str
    url: str
    thumbnailUrl: str

    def assert_valid(
            self,
            expected_id: Optional[int] = None,
            expected_album_id: Optional[int] = None,
            expected_title: Optional[str] = None,
            expected_url: Optional[str] = None,
            expected_thumbnail_url: Optional[str] = None,
    ):
        self.assert_field("id", expected_id, self.id)
        self.assert_field("albumId", expected_album_id, self.albumId)
        self.assert_field("title", expected_title, self.title, non_empty=True)
        self.assert_field("url", expected_url, self.url, non_empty=True)
        self.assert_field("thumbnailUrl", expected_thumbnail_url, self.thumbnailUrl, non_empty=True)