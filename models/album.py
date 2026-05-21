from typing import Optional
from models.base_api_model import BaseAPIModel


class Album(BaseAPIModel):
    userId: int
    id: int
    title: str

    def assert_valid(
        self,
        expected_id: Optional[int] = None,
        expected_user_id: Optional[int] = None,
        expected_title: Optional[str] = None
    ):
        self.assert_field("id", expected_id, self.id)
        self.assert_field("userId", expected_user_id, self.userId)
        self.assert_field("title", expected_title, self.title, non_empty=True)
