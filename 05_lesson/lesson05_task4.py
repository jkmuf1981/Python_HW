from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Firefox()

browser.get("http://the-internet.herokuapp.com/login")
username_field = browser.find_element(By.ID, "username")
password_field = browser.find_element(By.ID, "password")
login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

username_field.send_keys("tomsmith")
password_field.send_keys("SuperSecretPassword!")
login_button.click()

success_message = browser.find_element(By.CLASS_NAME, "flash.success").text
print(success_message)

browser.quit()
