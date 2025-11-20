from selenium.webdriver.common.by import By


class CheckoutStepOne:
    """
    Контакная информация клиента
    """
    def __init__(self, browser):
        self._driver = browser

    def filling_form(self, first_name, last_name, zip_code):
        """
        Заполняет регистрационную форму автоматически.

        Параметры:
        - user_data: словарь с ключами ('name', 'email', 'phone', 'password')
        """
        self._driver.find_element(By.CSS_SELECTOR, "#first-name").\
            send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "#last-name").\
            send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "#postal-code").\
            send_keys(zip_code)

    def click_continue(self):
        """
        Ищет кнопку 'Continue' и нажимает её.
        Затем проверяет, была ли страница обновлена.
        """
        self._driver.find_element(By.CSS_SELECTOR, "#continue").click()