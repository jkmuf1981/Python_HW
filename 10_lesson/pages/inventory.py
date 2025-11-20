from selenium.webdriver.common.by import By


class Inventory:

    def __init__(self, browser):
        self._driver = browser

    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#add-to-cart-sauce-labs-backpack").\
            click()
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#add-to-cart-sauce-labs-bolt-t-shirt").\
            click()
        self._driver.find_element(By.CSS_SELECTOR,
                                  "#add-to-cart-sauce-labs-onesie").\
            click()

    def go_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").\
            click()