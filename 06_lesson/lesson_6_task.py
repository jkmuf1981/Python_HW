from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()


# Переходим на нужную страницу
driver.get('http://uitestingplayground.com/ajax')

# Ищем синюю кнопку и нажимаем её
blue_button = driver.find_element(By.XPATH, '//button[@id="ajaxButton"]')
blue_button.click()

# Ждем появление зелёного блока с сообщением
green_box = WebDriverWait(driver, 15).until(  # увеличили таймаут до 15 сек
    EC.visibility_of_element_located((By.CLASS_NAME, 'bg-success'))
)

# Получаем текст из блока
text_from_green_box = green_box.text.strip()

# Проверяем и выводим сообщение
# text_from_green_box == "Data loaded with AJAX get request.":
print(text_from_green_box)
print(f"Полученный текст отличается: {text_from_green_box}")

# Закрываем браузер
driver.quit()