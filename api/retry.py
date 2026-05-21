import logging
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)

class LoggedRetry(Retry):
    def increment(self, method=None, url=None, response=None, *args, **kwargs):
        if response:
            logger.warning(
                f"Retry attempt {self.total} — {method} {url} returned {response.status}"
            )
        return super().increment(method, url, response, *args, **kwargs)