from selenium.webdriver.common.by import By


class Cart:
    """
    Класс по работе с корзиной
    """

    def __init__(self, browser):
        self._driver = browser

    def checkout(self):
        """
        оформление заказа
        """
        self._driver.find_element(By.CSS_SELECTOR, "#checkout").click()