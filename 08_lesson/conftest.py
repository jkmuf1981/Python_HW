
import pytest


@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com"  # Укажи реальный URL сервиса


@pytest.fixture(scope="session")
def auth_headers():
    token = "Укажите свой токен"

    return {"Authorization": f"Bearer {token}"}
