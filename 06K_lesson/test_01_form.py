from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
service = Service()
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

try:
    # Открываем нужную страницу
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    # Дожидаемся появления формы
    wait = WebDriverWait(driver, 20)  # Увеличили таймаут до 20 секунд
    first_name_field = wait.until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    # Другие поля остаются такими же
    last_name_field = driver.find_element(By.ID, "last-name")
    address_field = driver.find_element(By.ID, "address")
    email_field = driver.find_element(By.ID, "email")
    phone_number_field = driver.find_element(By.ID, "phone-number")
    zip_code_field = driver.find_element(By.ID, "zip-code")
    city_field = driver.find_element(By.ID, "city")
    country_field = driver.find_element(By.ID, "country")
    job_position_field = driver.find_element(By.ID, "job-position")
    company_field = driver.find_element(By.ID, "company")
    submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")

    # Заполняем форму
    first_name_field.send_keys("Иван")
    last_name_field.send_keys("Петров")
    address_field.send_keys("Ленина, 55-3")
    email_field.send_keys("test@skypro.com")
    phone_number_field.send_keys("+7985899998787")
    # Оставляем Zip Code пустым
    city_field.send_keys("Москва")
    country_field.send_keys("Россия")
    job_position_field.send_keys("QA")
    company_field.send_keys("SkyPro")

    # Отправляем форму
    submit_button.click()

    # Проверяем поля
    success_class = "has-success"
    error_class = "has-error"

    def check_field_color(field_id, expected_class):
        field = driver.find_element(By.ID, field_id)
        class_value = field.get_attribute('class')
        assert expected_class in class_value, \
            f"{field_id} не окрашено нужным цветом."

    # Проверяем цвет полей
    check_field_color("first-name", success_class)
    check_field_color("last-name", success_class)
    check_field_color("address", success_class)
    check_field_color("email", success_class)
    check_field_color("phone-number", success_class)
    check_field_color("city", success_class)
    check_field_color("country", success_class)
    check_field_color("job-position", success_class)
    check_field_color("company", success_class)

    # Поле ZIP должно быть красным (ошибочным)
    check_field_color("zip-code", error_class)

finally:
    # Закрытие окна браузера
    driver.quit()
