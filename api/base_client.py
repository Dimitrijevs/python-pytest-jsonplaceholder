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

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = self.session.get(url, timeout=10, **kwargs)
        logger.info(f"Response: {response.status_code}")
        return response

    def post(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        response = self.session.post(url, json=data, timeout=10)
        return response

    def put(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        response = self.session.put(url, json=data, timeout=10)
        logger.info(f"Response: {response.status_code}")
        return response

    def patch(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url}")
        response = self.session.patch(url, json=data, timeout=10)
        logger.info(f"Response: {response.status_code}")
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url, timeout=10)
        logger.info(f"Response: {response.status_code}")
        return response