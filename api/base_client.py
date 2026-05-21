import requests
import logging
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from api.retry import LoggedRetry
import os

load_dotenv()
logger = logging.getLogger(__name__)

class BaseClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.session = requests.Session()

        retry = LoggedRetry(
            total=3,
            backoff_factor=1,  # wait 1s, 2s, 4s between retries
            status_forcelist=[500, 502, 503, 504],  # retry on these status codes
            raise_on_status = False
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

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