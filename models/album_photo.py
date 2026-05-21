from pydantic import BaseModel

class AlbumPhoto(BaseModel):
    albumId: int
    id: int
    title: str
    url: str
    thumbnailUrl: str