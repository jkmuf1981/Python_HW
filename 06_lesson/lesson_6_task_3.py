from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера браузера (используем Chrome)
driver = webdriver.Chrome()

# Переходим на нужную страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ждём загрузки страницы
wait = WebDriverWait(driver, 30)  # Увеличенное время ожидания

# Ожидаем появления ровно 4-х изображений
wait.until(lambda d: len(d.find_elements(By.CSS_SELECTOR, 'img')) == 4)

# Получаем список всех изображений
images = driver.find_elements(By.CSS_SELECTOR, 'img')

# Проверяем загрузку каждого изображения
for i, img in enumerate(images[:4], start=1):  # Добавлен номер изображения
    src_attr = img.get_attribute('src')
    print(f"Проверяю изображение №{i}, src={src_attr}")  # Промежуточный вывод
    wait.until(lambda d: img.is_displayed() and len(src_attr.strip()) > 0)

# Извлекаем атрибут src у третьей картинки (индексация с нуля!)
third_image_src = images[2].get_attribute('src')
print(f"Атрибут src третьей картинки: {third_image_src}")

# Оставляем браузер открытым до ввода данных пользователем
input("Нажмите Enter, чтобы закрыть браузер...")

# Закрываем браузер
driver.quit()
