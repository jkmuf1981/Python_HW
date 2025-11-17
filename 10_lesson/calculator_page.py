import os
import sys
sys.path.insert(0, os.path.abspath(''))  # Включаем корневую папку проекта в PATH
from pages import CalculatorPage  # Этот вариант сработает, если будет отдельная папка `pages`
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """
    Класс для взаимодействия с веб-калькулятором.

    Attributes:
        BUTTON_7_LOCATOR (tuple): Локатор кнопки '7'.
        BUTTON_PLUS_LOCATOR (tuple): Локатор кнопки '+'.
        BUTTON_8_LOCATOR (tuple): Локатор кнопки '8'.
        BUTTON_EQUALS_LOCATOR (tuple): Локатор кнопки '='.
        RESULT_FIELD_LOCATOR (tuple): Локатор поля вывода результата.

    Methods:
        __init__: Инициализация объекта страницы.
        click_button: Кликает по кнопке с указанным локатором.
        wait_until_ready_state_complete: Ожидает полной загрузки страницы.
        set_delay: Эмулирует задержку перед выполнением действий.
        get_result: Получает значение из поля результата.
    """

    BUTTON_7_LOCATOR = (By.XPATH, "//button[@value='7']")
    BUTTON_PLUS_LOCATOR = (By.XPATH, "//button[@value='+']")
    BUTTON_8_LOCATOR = (By.XPATH, "//button[@value='8']")
    BUTTON_EQUALS_LOCATOR = (By.XPATH, "//button[@value='=']")
    RESULT_FIELD_LOCATOR = (By.ID, "result_field_id")  # Предположим, ID поля результата

    def __init__(self, browser):
        """
        Конструктор класса.

        :param browser: Объект браузера Selenium.
        """
        self.browser = browser

    def click_button(self, locator):
        """
        Выполняет клик по элементу на странице.

        :param locator: Локатор элемента для клика.
        """
        button = self.browser.find_element(*locator)
        button.click()

    def wait_until_ready_state_complete(self):
        """
        Ожидание завершения загрузки страницы.
        """
        WebDriverWait(self.browser, 30).until(
            lambda x: x.execute_script("return document.readyState") == "complete"
        )

    def set_delay(self, seconds):
        """
        Эмуляция задержки перед действиями.

        :param seconds: Количество секунд ожидания.
        """
        import time
        time.sleep(seconds)

