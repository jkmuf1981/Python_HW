import unittest
from selenium import webdriver
from .pages import *


class TestShop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Используйте нужный вам веб-драйвер
        self.driver.get("https://www.saucedemo.com/")

    def tearDown(self):
        self.driver.quit()

    def test_add_products_and_check_total(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_login_button()

        product_page = ProductPage(self.driver)
        products = ['Sauce Labs Backpack', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Onesie']
        for product in products:
            product_page.add_to_cart_by_name(product)

        product_page.go_to_cart()

        cart_page = CartPage(self.driver)
        cart_page.checkout()

        checkout_step_one_page = CheckoutStepOnePage(self.driver)
        checkout_step_one_page.fill_first_name('John')
        checkout_step_one_page.fill_last_name('Doe')
        checkout_step_one_page.fill_postal_code('12345')
        checkout_step_one_page.continue_checkout()

        overview_page = CheckoutOverviewPage(self.driver)
        total_amount = overview_page.get_total_price()

        expected_total = 58.29
        assert abs(
            total_amount - expected_total) <= 0.01, f'Total amount is incorrect: {total_amount}, expected: {expected_total}'


if __name__ == '__main__':
    unittest.main()