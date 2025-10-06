from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()

browser.get("http://uitestingplayground.com/dynamicid")
button = browser.find_element(By.CLASS_NAME, "btn-primary")
button.click()

browser.quit()
