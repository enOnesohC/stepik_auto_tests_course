from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#browser = webdriver.Chrome()
#link = "http://suninjuly.github.io/registration1.html"
#browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/registration2.html'
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    f_name = browser.find_element(By.CSS_SELECTOR, ".first[required]")
    f_name.send_keys("First Name")
    l_name = browser.find_element(By.CSS_SELECTOR, ".second[required]")
    l_name.send_keys("Last Name")
    e_mail = browser.find_element(By.CSS_SELECTOR, ".third[required]")
    e_mail.send_keys("test@test.test")
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(5)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

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
