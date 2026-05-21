from pydantic import BaseModel


class BaseAPIModel(BaseModel):

    def assert_field(self, field_name: str, expected_value, actual_value, non_empty: bool = False):
        if expected_value is not None:
            assert actual_value == expected_value, f"Expected {field_name}={expected_value}, got {actual_value}"
        elif non_empty:
            assert actual_value != "", f"{field_name} cannot be an empty string"