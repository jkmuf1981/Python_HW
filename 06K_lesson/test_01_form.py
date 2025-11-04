import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера"""
    service = Service()
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


def test_form_validation(driver):
    """Тест проверки валидации формы"""
    # Открываем нужную страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Дожидаемся появления формы
    wait = WebDriverWait(driver, 20)
    first_name_field = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )

    # Находим остальные поля
    last_name_field = driver.find_element(By.NAME, "last-name")
    address_field = driver.find_element(By.NAME, "address")
    email_field = driver.find_element(By.NAME, "e-mail")
    phone_number_field = driver.find_element(By.NAME, "phone")
    zip_code_field = driver.find_element(By.NAME, "zip-code")
    city_field = driver.find_element(By.NAME, "city")
    country_field = driver.find_element(By.NAME, "country")
    job_position_field = driver.find_element(By.NAME, "job-position")
    company_field = driver.find_element(By.NAME, "company")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary")

    # Заполняем форму
    first_name_field.send_keys("Иван")
    last_name_field.send_keys("Петров")
    address_field.send_keys("Ленина, 55-3")
    email_field.send_keys("test@skypro.com")
    phone_number_field.send_keys("+7985899998787")
    # Оставляем Zip Code пустым
    city_field.send_keys("Москва")
    country_field.send_keys("Россия")
    job_position_field.send_keys("QA")
    company_field.send_keys("SkyPro")

    # Отправляем форму
    # Используем JavaScript для клика, так как кнопка может быть перекрыта
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    # Проверяем поля
    success_class = "alert-success"
    error_class = "alert-danger"

    def check_field_color(field_id, expected_class):
        field = driver.find_element(By.ID, field_id)
        class_value = field.get_attribute('class')
        assert expected_class in class_value, \
            f"Поле {field_id} не имеет ожидаемый класс {expected_class}. Текущий класс: {class_value}"

    # Проверяем цвет полей (все должны быть зелеными, кроме zip-code)
    check_field_color("first-name", success_class)
    check_field_color("last-name", success_class)
    check_field_color("address", success_class)
    check_field_color("e-mail", success_class)
    check_field_color("phone", success_class)
    check_field_color("city", success_class)
    check_field_color("country", success_class)
    check_field_color("job-position", success_class)
    check_field_color("company", success_class)

    # Поле ZIP должно быть красным (ошибочным)
    check_field_color("zip-code", error_class)