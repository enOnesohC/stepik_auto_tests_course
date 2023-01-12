from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x_element_value = float(x_element.get_attribute("valuex"))
    #проверка, шо всё корректно работает
    #print("_________________________________________")
    #print(x_element_value)
    result = log(abs(12*sin(x_element_value)))
    #print(result)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка
