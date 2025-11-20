import allure
from selenium import webdriver
from pages.authorization import Authorization
from pages.inventory import Inventory
from pages.cart import Cart
from pages.checkout_step_one import CheckoutStepOne
from pages.checkout_step_two import CheckoutStepTwo


@allure.title("Покупка товара и оформление товара")
@allure.description("Тестирует добавление трёх товаров и оформление заказ.")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_internet_shop():
    username = "standard_user"
    password = "secret_sauce"
    first_name = "John"
    last_name = "Smith"
    zip_code = "33701-4313"

    with allure.step("Инициализация страницы"):
        browser = webdriver.Firefox()
        authorization_page = Authorization(browser)
    with allure.step("Авторизация"):
        authorization_page.authorization(username, password)

    with allure.step("Добавление товара и переход в корзину"):
        inventory_page = Inventory(browser)
        inventory_page.add_to_cart()
        inventory_page.go_to_cart()

    with allure.step("Начало оформления заказа"):
        cart_page = Cart(browser)
        cart_page.checkout()

    with allure.step("Ввод данных заказчика"):
        checkout_step_one_page = CheckoutStepOne(browser)
        checkout_step_one_page.filling_form(first_name, last_name, zip_code)
        checkout_step_one_page.click_continue()

    with allure.step("Получение итоговой суммы"):
        checkout_step_two_page = CheckoutStepTwo(browser)
        total = checkout_step_two_page.read_total()

    assert total[total.find("$"):] == "$58.29"

    browser.quit()
