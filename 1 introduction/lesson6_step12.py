from selenium import webdriver
from selenium.webdriver.common.by import By
import time



link = 'http://suninjuly.github.io/registration1.html'


try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ("[class='form-control first']"))
    input1.send_keys("Denis")
    input2 = browser.find_element(By.CSS_SELECTOR,("[input='text']"))
    input2.send_keys("denisplotkin95@gmail.com")
    input3 = browser.find_element(By.XPATH, ("//div[@class='second_block']//input[@class='form-control first']"))
    input3.send_keys("Phone")
    input4 = browser.find_element(By.XPATH, ("//div[@class='second_block']//input[@class='form-control second']"))
    input4.send_keys("Ukraine")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
