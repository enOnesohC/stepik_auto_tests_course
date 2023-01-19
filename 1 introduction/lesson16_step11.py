from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//[first_block//form-control.first'
    input1.send_keys("Andrey")

    input2 = browser.find_element(By.CLASS_NAME, "form-control.second")
    input2.send_keys("shrek")

    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("kek@shrek.kek")

    input4 = browser.find_element(By.XPATH, '//input[@placeholder = "Input your phone:"]')
    input4.send_keys("555-1234567890987654321")

    input5 = browser.find_element(By.XPATH, '//input[@placeholder = "Input your address:"]')
    input5.send_keys("SWAMP")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
