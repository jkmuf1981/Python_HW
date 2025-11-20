import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import CalculatorPage
import allure

# Фикстура браузера
@pytest.fixture(scope="module")
def browser():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Тестовый сценарий
@allure.title("Проверка операции сложения с задержкой")
@allure.description("Тестирует операцию 7+8 с ожиданием результата.")
@allure.feature("Арифметические операции")
@allure.severity(allure.severity_level.NORMAL)
def test_calculate_with_delay(browser):
    with allure.step("Инициализация страницы"):
        page = CalculatorPage(browser)

    with allure.step("Ожидание полной загрузки страницы"):
        page.wait_until_ready_state_complete()

    with allure.step("Установка задержки на выполнение операции"):
        page.set_delay(45)

    with allure.step("Нажатие нужных кнопок"):
        page.click_button(page.BUTTON_7_LOCATOR)
        page.click_button(page.BUTTON_PLUS_LOCATOR)
        page.click_button(page.BUTTON_8_LOCATOR)
        page.click_button(page.BUTTON_EQUALS_LOCATOR)

    with allure.step("Ожидание отображения правильного результата"):
        WebDriverWait(browser, 60).until(
            EC.text_to_be_present_in_element(page.RESULT_FIELD_LOCATOR, "15"),
            message="Результат не соответствует ожидаемому!"
        )