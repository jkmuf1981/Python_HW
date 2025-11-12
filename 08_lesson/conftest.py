import os
import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://ru.yougile.com"  # Реальный URL сервиса Yougile

@pytest.fixture(scope="session")
def auth_headers():
    token = os.getenv("YOUGILE_API_KEY")  # Получаем токен из переменной окружения
    if not token:
        raise ValueError("Environment variable YOUGILE_API_KEY must be set!")
    return {"Authorization": f"Bearer {token}"}