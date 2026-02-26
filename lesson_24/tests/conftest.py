import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"


def _setup_logger() -> logging.Logger:
    logger = logging.getLogger("cars_tests")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)

    fmt = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

    sh = logging.StreamHandler()
    sh.setFormatter(fmt)

    fh = logging.FileHandler("test_search.log", mode="w", encoding="utf-8")
    fh.setFormatter(fmt)

    logger.addHandler(sh)
    logger.addHandler(fh)
    return logger


@pytest.fixture(scope="session")
def logger() -> logging.Logger:
    return _setup_logger()


@pytest.fixture(scope="class")
def auth_session(request, logger):
    s = requests.Session()
    r = s.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass"),
        timeout=10,
    )
    logger.info(f"AUTH POST /auth status={r.status_code}")
    r.raise_for_status()
    token = r.json().get("access_token")
    if not token:
        raise RuntimeError(f"No access_token in response: {r.text}")
    s.headers.update({"Authorization": f"Bearer {token}"})
    request.cls.session = s
    request.cls.base_url = BASE_URL
    request.cls.logger = logger
    yield s
    s.close()