import allure
from selenium import webdriver
from pages.slow_calculator import SlowCalculator



@allure.title("Проверка операции сложения с задержкой")
@allure.description("Тестирует операцию 7+8 с ожиданием результата.")
@allure.feature("Арифметические операции")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator():
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    timeout = 45
    with allure.step("Инициализация страницы"):
        browser = webdriver.Chrome()
        main_page = SlowCalculator(browser, url)
    with allure.step("Установка задержки на выполнение операции"):
        main_page.set_timeout(timeout)
    with allure.step("Нажатие нужных кнопок"):
        main_page.pressing_buttons()
    with allure.step("Ожидание отображения правильного результата"):
        to_be = main_page.result()
    assert to_be == 15

    browser.quit()
