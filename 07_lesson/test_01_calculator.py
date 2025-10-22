import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # добавляем импорт
from selenium.webdriver.support import expected_conditions as EC  # добавляем импорт
from calculator_page import CalculatorPage


class TestSlowCalculator(unittest.TestCase):
    def setUp(self):
        # Инициализация драйвера
        self.driver = webdriver.Chrome()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.calculator_page = CalculatorPage(self.driver)

    def test_calculate_with_delay(self):
        """
        Тестирует выражение 7 + 8 с задержкой 45 секунд.
        Ожидается результат 15 после истечения времени задержки.
        """
        # Устанавливаем задержку в 45 секунд
        self.calculator_page.set_delay('45')

        # Кликаем по кнопкам калькулятора
        self.calculator_page.click_button(CalculatorPage.BUTTON_7_LOCATOR)
        self.calculator_page.click_button(CalculatorPage.BUTTON_PLUS_LOCATOR)
        self.calculator_page.click_button(CalculatorPage.BUTTON_8_LOCATOR)
        self.calculator_page.click_button(CalculatorPage.BUTTON_EQUALS_LOCATOR)

        # Ждём результат
        wait = WebDriverWait(self.driver, 50)  # дожидаемся результата в течение 50 секунд
        result = wait.until(lambda x: self.calculator_page.get_result())  # сократили длинную строку

        # Проверяем результат
        self.assertEqual(result, '15',
                         f'Ожидался результат "15", а получилось "{result}"')  # перенесли строку

    def tearDown(self):
        # Закрываем браузер после окончания теста
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

# Добавляем пустую строку в конце файла