
import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com"  # Укажи реальный URL сервиса


@pytest.fixture(scope="session")
def auth_headers():
    token = "ReW6lYqS2lcSxinJtKFvQ60PV1Onxoe6Nzad82s5COBUvkUn8as7oZ6ZJVLoc2tJ"

    return {"Authorization": f"Bearer {token}"}
