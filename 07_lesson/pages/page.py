from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        """Метод вводит имя пользователя"""
        self.driver.find_element(By.ID, 'user-name').send_keys(username)

    def enter_password(self, password):
        """Метод вводит пароль"""
        self.driver.find_element(By.ID, 'password').send_keys(password)

    def click_login_button(self):
        """Метод нажимает кнопку входа"""
        self.driver.find_element(By.ID, 'login-button').click()




class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_by_name(self, product_name):
        """Метод добавляет товар в корзину по названию товара"""
        xpath_selector = f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button'
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath_selector))
            )
            button.click()
        except Exception as e:
            print(f"Error adding item '{product_name}' to the cart: {e}")

    def go_to_cart(self):
        """Метод открывает страницу корзины"""
        cart_icon = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart_icon.click()




class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        """Метод инициирует оформление покупки"""

        wait = WebDriverWait(self.driver, 15)
        wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn_action.checkout_button"))
        ).click()




class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver

    def fill_first_name(self):
        """Метод инициирует оформление покупки"""

        wait = WebDriverWait(self.driver, 15)
        wait.until(
        EC.element_to_be_clickable((By.ID, "first-name"))
                                    ).send_keys("John")

    def fill_last_name(self, last_name):
        """Метод вводит фамилию покупателя"""
        wait = WebDriverWait(self.driver, 15)
        wait.until(
            EC.element_to_be_clickable((By.ID, "last-name"))
        ).send_keys(last_name)


    def fill_postal_code(self, postal_code):
        """Метод вводит почтовый индекс"""
        wait = WebDriverWait(self.driver, 15)
        wait.until(
            EC.element_to_be_clickable((By.ID, 'postal-code'))
        ).send_keys(postal_code)


    def continue_checkout(self):
        """Метод продолжает процесс оформления заказа"""
        self.driver.find_element(By.CSS_SELECTOR, '.cart_button').click()


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_price(self):
        """Метод возвращает итоговую сумму заказа"""
        total_text = self.driver.find_element(By.CLASS_NAME, 'summary_total_label').text
        return float(total_text.split('$')[-1])