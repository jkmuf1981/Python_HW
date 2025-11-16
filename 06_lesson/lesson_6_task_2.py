from selenium import webdriver
from selenium.webdriver.common.by import By

# Создание экземпляра драйвера Chrome
driver = webdriver.Chrome()


# Переход на нужную страницу
driver.get('http://uitestingplayground.com/textinput')

# Поиск поля ввода и ввод значения "SkyPro"
input_field = driver.find_element(By.ID, 'newButtonName')  # ID поля ввода
input_field.clear()  # Очистка текущего содержимого (если вдруг заполнено)
input_field.send_keys('SkyPro')

# Поиск синей кнопки и клик по ней
submit_button = driver.find_element(By.ID, 'updatingButton')  # ID кнопки
submit_button.click()

# Получение нового названия кнопки
new_button_text = submit_button.text.strip()

# Проверка и вывод полученного имени кнопки
# new_button_text == "SkyPro":
print(new_button_text)

print(f"Произошла ошибка: кнопка стала '{new_button_text}' вместо 'SkyPro'")

# Закрытие браузера
driver.quit()
