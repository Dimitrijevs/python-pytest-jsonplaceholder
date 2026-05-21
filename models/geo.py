from pydantic import BaseModel


class Geo(BaseModel):
    lat: str
    lng: str