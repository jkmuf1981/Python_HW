# Файл: pages/calculator_page.py

from selenium.webdriver.common.by import By

class CalculatorPage:
    BUTTON_7_LOCATOR = (By.XPATH, "//button[@value='7']")
    BUTTON_PLUS_LOCATOR = (By.XPATH, "//button[@value='+']")
    BUTTON_8_LOCATOR = (By.XPATH, "//button[@value='8']")
    BUTTON_EQUALS_LOCATOR = (By.XPATH, "//button[@value='=']")
    RESULT_FIELD_LOCATOR = (By.ID, "result_field_id")  # Предположим, ID поля результата

    def __init__(self, browser):
        self.browser = browser

    def click_button(self, locator):
        button = self.browser.find_element(*locator)
        button.click()

    def wait_until_ready_state_complete(self):
        WebDriverWait(self.browser, 30).until(
            lambda x: x.execute_script("return document.readyState") == "complete"
        )

    def set_delay(self, seconds):
        # Здесь мы эмулируем задержку (при условии, что приложение само её не реализует)
        import time
        time.sleep(seconds)

    def get_result(self):
        return self.browser.find_element(*self.RESULT_FIELD_LOCATOR).text.strip()

    def get_result(self):
        """Получает результат из окна калькулятора."""
        return self.driver.find_element(*self.RESULT_FIELD_LOCATOR).text.strip()