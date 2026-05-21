from typing import Optional
from models.base_api_model import BaseAPIModel
from models.address import Address
from models.company import Company
from pydantic import EmailStr


class User(BaseAPIModel):
    id: int
    name: str
    username: str
    email: EmailStr
    address: Address
    phone: str
    website: str
    company: Company

    def assert_valid(
            self,
            expected_id: Optional[int] = None,
            expected_name: Optional[str] = None,
            expected_username: Optional[str] = None,
            expected_email: Optional[str] = None,
            expected_phone: Optional[str] = None,
            expected_website: Optional[str] = None,
    ):
        self.assert_field("id", expected_id, self.id)
        self.assert_field("name", expected_name, self.name, non_empty=True)
        self.assert_field("username", expected_username, self.username, non_empty=True)
        self.assert_field("email", expected_email, self.email, non_empty=True)
        self.assert_field("phone", expected_phone, self.phone, non_empty=True)
        self.assert_field("website", expected_website, self.website, non_empty=True)
