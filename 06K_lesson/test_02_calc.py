import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def setup():
    """Инициализация браузера Chrome."""
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_calculator(setup):
    """Автотест калькулятора."""
    driver = setup
    try:
        # Открываем страницу калькулятора
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Установка задержки (45 секунд)
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # Правильные локаторы кнопок калькулятора
        button_seven = driver.find_element(By.XPATH, "//span[text()='7']")
        button_plus = driver.find_element(By.XPATH, "//span[text()='+']")
        button_eight = driver.find_element(By.XPATH, "//span[text()='8']")
        button_equal = driver.find_element(By.XPATH, "//span[text()='=']")

        # Последовательно нажимаем кнопки
        button_seven.click()
        button_plus.click()
        button_eight.click()
        button_equal.click()

        # Ждём появления результата (до 50 секунд)
        wait = WebDriverWait(driver, 50)
        result_display = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

        # Проверяем результат
        final_result = driver.find_element(By.CLASS_NAME, "screen").text
        assert final_result == "15", f"Результат не совпал с ожиданием: {final_result}"

    except Exception as e:
        print(f"Возникла ошибка: {e}")
        raise