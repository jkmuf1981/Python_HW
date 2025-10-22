from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    # Локаторы элементов
    DELAY_INPUT_LOCATOR = (By.ID, 'delay')
    RESULT_FIELD_LOCATOR = (By.CSS_SELECTOR, '.screen')
    BUTTON_7_LOCATOR = (By.XPATH, "//button[.='7']")  # Новый локатор
    BUTTON_PLUS_LOCATOR = (By.XPATH, "//button[@value='+']")
    BUTTON_8_LOCATOR = (By.XPATH, "//button[@value='8']")
    BUTTON_EQUALS_LOCATOR = (By.XPATH, "//button[@value='=']")

    # остальные методы остаются без изменений

    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay_value):
        input_field = self.driver.find_element(*self.DELAY_INPUT_LOCATOR)
        input_field.clear()
        input_field.send_keys(str(delay_value))

    def click_button(self, button_locator):
        button = WebDriverWait(self.driver, 45).until(  # увеличенное время ожидания
            EC.element_to_be_clickable(button_locator)
        )
        button.click()

    def get_result(self):
        result_field = self.driver.find_element(*self.RESULT_FIELD_LOCATOR)
        return result_field.text.strip()