import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="session")
def setup():
    """Инициализация драйвера Firefox."""
    service = Service()
    options = Options()
    options.add_argument("--headless")  # Безголовое исполнение (если нужно)
    options.add_argument("--disable-gpu")  # Отключаем ускорение графическим процессором
    options.add_argument("--window-size=1920,1080")  # Стандартный размер окна
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()


def test_purchase(setup):
    """Автотест покупки на SauceDemo."""
    driver = setup
    try:
        # Открываем главную страницу
        driver.get("https://www.saucedemo.com/")

        # Авторизуемся как standard_user
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        # Добавляем товары в корзину
        product_names = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for product_name in product_names:
            add_to_cart_button = driver.find_element(By.XPATH,
                                                     f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
            add_to_cart_button.click()

        # Переходим в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # Начинаем оформление заказа
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Заполняем контактные данные
        first_name_field = driver.find_element(By.ID, "first-name")
        last_name_field = driver.find_element(By.ID, "last-name")
        postal_code_field = driver.find_element(By.ID, "postal-code")
        continue_button = driver.find_element(By.ID, "continue")

        first_name_field.send_keys("John")
        last_name_field.send_keys("Doe")
        postal_code_field.send_keys("12345")
        continue_button.click()

        # Получаем итоговую сумму
        total_amount = driver.find_element(By.CLASS_NAME, "summary_total_label").text
        expected_total = "$58.29"

        # Проверяем, что итоговая сумма верна
        assert total_amount.endswith(expected_total), f"Итоговая сумма не совпала с ожиданием: {total_amount}"

    except Exception as e:
        print(f"Возникла ошибка: {e}")
        raise