import requests
import logging
from dotenv import load_dotenv
import os

load_dotenv()
logger = logging.getLogger(__name__)

class BaseClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.session = requests.Session()

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"{method} {url}")
        response = self.session.request(method, url, timeout=10, **kwargs)
        logger.info(f"Response: {response.status_code}")
        return response

    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, data: dict):
        return self._request("POST", endpoint, json=data)

    def put(self, endpoint: str, data: dict):
        return self._request("PUT", endpoint, json=data)

    def patch(self, endpoint: str, data: dict):
        return self._request("PATCH", endpoint, json=data)

    def delete(self, endpoint: str):
        return self._request("DELETE", endpoint)