from pydantic import BaseModel
from models.geo import Geo


class Address(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: Geo
