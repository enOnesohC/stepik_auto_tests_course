from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import *

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 20 секунд, пока текст не станет равным 100
    time = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button_ec = browser.find_element(By.ID, "book")
    button_ec.click()

    #проводим вычисления

    x_element = browser.find_element(By.ID, "input_value")
    x = float(x_element.text)
    result = log(abs(12*sin(x)))

    #вставка результата в поле

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(result)

    # нажатие на кнопку
    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# пустая строка
