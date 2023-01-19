from selenium import webdriver
from selenium.webdriver.common.by import By
import time



link = 'http://suninjuly.github.io/registration2.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ("[class='form-control first']"))
    input1.send_keys("Denis")
    input2 = browser.find_element(By.CSS_SELECTOR, ("[class='form-control second']"))
    input2.send_keys("Dayn")
    input3 = browser.find_element(By.CSS_SELECTOR, ("[class='form-control third']"))
    input3.send_keys("denisplotkin95@gmail.com")
    input4 = browser.find_element(By.XPATH, ("//div[@class='second_block']//input[@class='form-control first']"))
    input4.send_keys("0634202456")
    input5 = browser.find_element(By.XPATH, ("//div[@class='second_block']//input[@class='form-control second']"))
    input5.send_keys("Kyiv")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
