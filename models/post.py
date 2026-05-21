from models.base_api_model import BaseAPIModel
from typing import Optional


class Post(BaseAPIModel):
    id: int
    userId: int
    title: str
    body: str

    def assert_valid(
        self,
        expected_id: Optional[int] = None,
        expected_user_id: Optional[int] = None,
        expected_title: Optional[str] = None,
        expected_body: Optional[str] = None
    ):
        self.assert_field("id", expected_id, self.id)
        self.assert_field("userId", expected_user_id, self.userId)
        self.assert_field("title", expected_title, self.title, non_empty=True)
        self.assert_field("body", expected_body, self.body, non_empty=True)