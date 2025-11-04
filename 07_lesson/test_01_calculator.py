# Файл: tests/test_01_calculator.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.calculator_page import CalculatorPage # Правильный импорт класса страницы

@pytest.fixture(scope="module")
def browser():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_calculate_with_delay(browser):
    """Тестируем выражение 7 + 8 с задержкой 45 секунд"""
    page = CalculatorPage(browser)

    # Полностью ждём загрузку страницы
    page.wait_until_ready_state_complete()

    # Добавляем задержку на выполнение операций
    page.set_delay(45)

    # Нажимаем нужные кнопки
    page.click_button(page.BUTTON_7_LOCATOR)
    page.click_button(page.BUTTON_PLUS_LOCATOR)
    page.click_button(page.BUTTON_8_LOCATOR)
    page.click_button(page.BUTTON_EQUALS_LOCATOR)

    # Ждём появления результата
    WebDriverWait(browser, 60).until(
        EC.text_to_be_present_in_element(page.RESULT_FIELD_LOCATOR, "15"),
        message="Результат не соответствует ожидаемому!"
    )