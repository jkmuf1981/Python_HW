from selenium.webdriver.common.by import By


class Authorization:
    """
    Класс авторизации в магазине
    """
    def __init__(self, browser):
        self._driver = browser
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    def authorization(self, username, password):
        """
        Авторизация на странице маагзина
        """
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]').\
            send_keys("standard_user")
        self._driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').\
            send_keys("secret_sauce")
        self._driver.find_element(By.CSS_SELECTOR,
                                  'input[id="login-button"]').click()