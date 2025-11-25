from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SlowCalculator:
    """
       Класс для взаимодействия с веб-калькулятором.

       Methods:
           __init__: Инициализация объекта страницы.
          set_timeout: установка задержки калькулятора.
          pressing_buttons: нажатие на заданные кнопки калькулятора.
          result: получение результата вычисленний.
       """
    def __init__(self, browser, url):
        self._driver = browser
        self._driver.get(url)
        self._driver.maximize_window()

    def set_timeout(self, timeout):
        """
          В поле ввода по локатору #delay вводим значение 45.
         """

        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").\
            send_keys(str(timeout))

    def pressing_buttons(self):
        """
        нажатие на заданные кнопки калькулятора
        вычисления 7+8
        """
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[1]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[4]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[2]').\
            click()
        self._driver.find_element(By.XPATH,
                                  '//*[@id="calculator"]/div[2]/span[15]').\
            click()
        waiter = WebDriverWait(self._driver, 46)
        waiter.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.screen'), '15'))

    def result(self):
        """
         получение результата вычисленний.
        """
        txt = self._driver.find_element(By.CSS_SELECTOR, '.screen').text

        return int(txt)