from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Создаем экземпляр драйвера Chrome
driver = webdriver.Chrome()

# Переход на нужную страницу
driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

# Ожидаем, пока загрузятся все три изображения
WebDriverWait(driver, 30).until(
    lambda d: len(d.find_elements(By.TAG_NAME, 'img')) >= 3
)

# Получаем список всех изображений
images = driver.find_elements(By.TAG_NAME, 'img')

# Третья картинка (индексация с 0)
third_image = images[2]

# Получаем значение атрибута src
image_src = third_image.get_attribute('src')

# Выводим значение атрибута в консоль
print(image_src)

# Закрытие браузера
driver.quit()