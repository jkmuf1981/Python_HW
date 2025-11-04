import pytest
from selenium import webdriver
from pages.page import LoginPage, ProductPage, CartPage, CheckoutStepOnePage, CheckoutOverviewPage


@pytest.fixture(scope="module")
def driver():
    """Фикстура для запуска браузера"""
    driver = webdriver.Edge()  # Используйте нужный вам драйвер
    yield driver
    driver.quit()


def test_add_products_and_check_total(driver):
    """
    Проверяет процесс добавления товаров в корзину,
    прохождение шагов оформления заказа и итоговую сумму покупки.
    """
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login_button()

    product_page = ProductPage(driver)
    products = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
    for product in products:
        product_page.add_to_cart_by_name(product)

    product_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout()

    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_one_page.fill_first_name('John')
    checkout_step_one_page.fill_last_name('Doe')
    checkout_step_one_page.fill_postal_code('12345')
    checkout_step_one_page.continue_checkout()

    overview_page = CheckoutOverviewPage(driver)
    total_amount = overview_page.get_total_price()

    expected_total = 58.29
    assert abs(total_amount - expected_total) <= 0.01, \
        f'Итоговая сумма неверна: {total_amount}, ожидалось: {expected_total}'