from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    #вход на сайт
    link = "http://suninjuly.github.io/selects2.html?"
    browser = webdriver.Chrome()
    browser.get(link)

    #считывание чисел
    num1 = browser.find_element(By.ID, "num1")
    num1_value = int(num1.text)

    num2 = browser.find_element(By.ID, "num2")
    num2_value = int(num2.text)

    sum = num1_value + num2_value
    sum1 = str(sum)
    #print(num1_value)
    #print(num2_value)
    #print(sum1)

    #вход в список и поиск нужного элемента
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sum1)

    #browser.find_element(By.TAG_NAME, "select").click()
    #time.sleep(2)
    #browser.find_element(By.CSS_SELECTOR, "[value=sum1]").click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



# пустая строка
