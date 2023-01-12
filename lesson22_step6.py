from math import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    #вход на сайт
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #считывание чисел
    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)

    result = log(abs(12*sin(x)))
    result_value = str(result)

    #скроллинг

    #вход в список и поиск нужного элемента
    input1 = browser.find_element(By.ID, "answer")
    #скролл вниз до нужного элемента
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    #browser.execute_script("window.scrollTo(0, 99)")
    input1.send_keys(result)

    #browser.execute_script("window.scrollTo(0, 99)")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", input1)

    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()

    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    #time.sleep(1)
    #скролл вниз до нужного элемента
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)



    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



# пустая строка
