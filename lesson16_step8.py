from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"


browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element(By.NAME, "first_name")
input1.send_keys("Ivan")
input2 = browser.find_element(By.NAME, 'last_name')
input2.send_keys("Petrov")
input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
input3.send_keys("Smolensk")
input4 = browser.find_element(By.ID, "country")
input4.send_keys("Russia")

#https://habr.com/ru/post/250975/
button = browser.find_element(By.XPATH, '//button[text() = "Submit"]')
button.click()

    # успеваем скопировать код за 30 секунд

time.sleep(10)

    # закрываем браузер после всех манипуляций
browser.close()
browser.quit()

# не забываем оставить пустую строку в конце файла
