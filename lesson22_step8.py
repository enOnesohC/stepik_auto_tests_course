from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    #заходим на сайт
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполнение полей
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("kek")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("kekOvich")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("kek@shrek.kek")

    # приложение файла

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '123.txt')           # добавляем к этому пути имя файла

    #находим элемент с помощью селектора и кликаем
    element = browser.find_element(By.NAME, "file")
    element.send_keys(file_path)

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
