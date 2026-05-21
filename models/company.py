from pydantic import BaseModel


class Company(BaseModel):
    name: str
    catchPhrase: str
    bs: str