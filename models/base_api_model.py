from pydantic import BaseModel


class BaseAPIModel(BaseModel):

    def assert_field(self, field_name: str, expected_value, actual_value, non_empty: bool = False):
        if expected_value is not None:
            assert actual_value == expected_value, f"Expected {field_name}={expected_value}, got {actual_value}"
        elif non_empty:
            assert actual_value != "", f"{field_name} cannot be an empty string"

    @staticmethod
    def assert_status_code(response, expected_code: int):
        assert response.status_code == expected_code, \
            f"Expected status code {expected_code}, got {response.status_code}"

    @staticmethod
    def assert_empty_body(response):
        assert response.json() == {}, \
            f"Expected empty body {{}}, got {response.json()}"

    @staticmethod
    def assert_empty_list(response):
        assert response.json() == [], \
            f"Expected empty list [], got {response.json()}"