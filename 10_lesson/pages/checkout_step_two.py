from selenium.webdriver.common.by import By


class CheckoutStepTwo:
    """
    Выбор способа оплаты
    """
    def __init__(self, browser):
        self._driver = browser

    def read_total(self):
        """
        Ищем элемент общей суммы
        """

        total = self._driver.find_element(By.CSS_SELECTOR,
                                          ".summary_total_label").text

        return total