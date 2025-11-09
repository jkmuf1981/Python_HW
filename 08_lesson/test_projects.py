import requests
import pytest
from  utils import random_string

@pytest.mark.positive
def test_create_project(base_url, auth_headers):
    """Позитивный тест создания проекта"""
    payload = {
        "name": random_string(),
        "description": "This is my awesome test project."
    }
    response = requests.post(f"{base_url}/projects", json=payload, headers=auth_headers)
    assert response.status_code == 201, "Проект не был создан!"
    created_project = response.json()
    assert created_project['name'] == payload['name'], "Название проекта отличается от отправленного!"

@pytest.mark.negative
def test_create_project_without_required_fields(base_url, auth_headers):
    """Негативный тест: проверка реакции сервера на отсутствие необходимых полей"""
    payload = {}
    response = requests.post(f"{base_url}/projects", json=payload, headers=auth_headers)
    assert response.status_code in (400, 422), "Сервер принял пустой запрос!"

@pytest.mark.positive
def test_update_project(base_url, auth_headers):
    """Позитивный тест обновления проекта"""
    # Сначала создадим проект
    create_payload = {
        "name": random_string(),
        "description": "Original description"
    }
    creation_response = requests.post(f"{base_url}/projects", json=create_payload, headers=auth_headers)
    project_id = creation_response.json()['id']

    # Теперь обновляем созданный проект
    update_payload = {
        "name": random_string(),
        "description": "Updated description"
    }
    update_response = requests.put(f"{base_url}/projects/{project_id}", json=update_payload, headers=auth_headers)
    assert update_response.status_code == 200, "Проект не был обновлён!"
    updated_project = update_response.json()
    assert updated_project['name'] == update_payload['name'], "Имя проекта не было обновлено!"

@pytest.mark.negative
def test_update_non_existing_project(base_url, auth_headers):
    """Негативный тест: обновление несуществующего проекта"""
    fake_project_id = 9999999
    payload = {
        "name": random_string(),
        "description": "Non-existing project update attempt"
    }
    response = requests.put(f"{base_url}/projects/{fake_project_id}", json=payload, headers=auth_headers)
    assert response.status_code == 404, "Сервер обновил несуществующий проект!"

@pytest.mark.positive
def test_get_project_by_id(base_url, auth_headers):
    """Позитивный тест получения проекта по id"""
    # Сначала создадим проект
    create_payload = {
        "name": random_string(),
        "description": "Project to retrieve by id"
    }
    creation_response = requests.post(f"{base_url}/projects", json=create_payload, headers=auth_headers)
    project_id = creation_response.json()['id']

    # Получаем созданный проект
    get_response = requests.get(f"{base_url}/projects/{project_id}", headers=auth_headers)
    assert get_response.status_code == 200, "Проект не найден!"
    retrieved_project = get_response.json()
    assert retrieved_project['name'] == create_payload['name'], "Имена проектов различаются!"

@pytest.mark.negative
def test_get_non_existing_project(base_url, auth_headers):
    """Негативный тест: попытка получить несуществующий проект"""
    fake_project_id = 9999999
    response = requests.get(f"{base_url}/projects/{fake_project_id}", headers=auth_headers)
    assert response.status_code == 404, "Сервер нашёл несуществующий проект!"