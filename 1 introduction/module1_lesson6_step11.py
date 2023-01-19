from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html" # URL первой версии регистрации
    browser = webdriver.Chrome()
    browser.get(link)
    # Вводим имя
    first_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    first_name.send_keys('Qwerty')
    # Вводим фамилию
    last_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    last_name.send_keys('Asd')
    # Вводим электронный почтовый адрес
    email = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    email.send_keys('asd@asd.com')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

    # Спасибо за рецензию)
