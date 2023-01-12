from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    #заходим на сайт
    link = "https://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим кнопку с помощью селектора и кликаем
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

    #подтверждаем через метод confirm, так как есть и кнопка отмена, кроме подтверждения

    confirm = browser.switch_to.alert
    confirm.accept()

    #проводим вычисления

    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    result = log(abs(12*sin(x)))

    #вставка результата в поле

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    # нажатие на кнопку
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()

    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка
