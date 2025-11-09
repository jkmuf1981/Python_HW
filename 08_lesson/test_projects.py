import requests
import pytest
from  utils import random_string

@pytest.mark.positive
def test_create_project_positive(base_url, auth_headers):
    """Позитивный тест создания проекта"""
    payload = {
        "name": random_string(),
        "description": "Тестовый проект для автоматизации"
    }
    response = requests.post(f"{base_url}/api-v2/projects", json=payload, headers=auth_headers)
    assert response.status_code == 201, "Проект не был создан!"
    created_project = response.json()
    assert created_project['name'] == payload['name'], "Название проекта отличается от отправленного!"

@pytest.mark.positive
def test_get_project_positive(base_url, auth_headers):
    """Позитивный тест получения проекта"""
    # Создаем проект
    payload = {
        "name": random_string(),
        "description": "Тестовый проект для чтения"
    }
    creation_response = requests.post(f"{base_url}/api-v2/projects", json=payload, headers=auth_headers)
    project_id = creation_response.json()['id']

    # Читаем созданный проект
    response = requests.get(f"{base_url}/api-v2/projects/{project_id}", headers=auth_headers)
    assert response.status_code == 200, "Проект не найден!"
    retrieved_project = response.json()
    assert retrieved_project['name'] == payload['name'], "Название проекта отличается от исходного!"

@pytest.mark.positive
def test_update_project_positive(base_url, auth_headers):
    """Позитивный тест обновления проекта"""
    # Создаем проект
    payload = {
        "name": random_string(),
        "description": "Исходный проект"
    }
    creation_response = requests.post(f"{base_url}/api-v2/projects", json=payload, headers=auth_headers)
    project_id = creation_response.json()['id']

    # Обновляем проект
    update_payload = {
        "name": random_string(),
        "description": "Обновленный проект"
    }
    response = requests.put(f"{base_url}/api-v2/projects/{project_id}", json=update_payload, headers=auth_headers)
    assert response.status_code == 200, "Проект не был обновлен!"
    updated_project = response.json()
    assert updated_project['name'] == update_payload['name'], "Название проекта не изменилось!"

    @pytest.mark.negative
    def test_create_project_negative_empty_name(base_url, auth_headers):
        """Негативный тест: создание проекта с пустым именем"""
        payload = {
            "name": "",
            "description": "Без названия"
        }
        response = requests.post(f"{base_url}/api-v2/projects", json=payload, headers=auth_headers)
        assert response.status_code == 400, "Некорректный статус-код при создании проекта с пустым именем!"

    @pytest.mark.negative
    def test_get_nonexisting_project(base_url, auth_headers):
        """Негативный тест: получение несуществующего проекта"""
        invalid_id = 999999999  # заведомо несуществующий ID
        response = requests.get(f"{base_url}/api-v2/projects/{invalid_id}", headers=auth_headers)
        assert response.status_code == 404, "Сервис нашел несуществующий проект!"

    @pytest.mark.negative
    def test_update_nonexisting_project(base_url, auth_headers):
        """Негативный тест: обновление несуществующего проекта"""
        invalid_id = 999999999  # заведомо несуществующий ID
        payload = {
            "name": random_string(),
            "description": "Новый проект"
        }
        response = requests.put(f"{base_url}/api-v2/projects/{invalid_id}", json=payload, headers=auth_headers)
        assert response.status_code == 404, "Сервер обновил несуществующий проект!"