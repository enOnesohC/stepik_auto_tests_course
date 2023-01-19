from selenium import webdriver
from selenium.webdriver.common.by import By
import math


Math = str(math.ceil(math.pow(math.pi, math.e)*10000))
print(Math)

i = 0

while i < 10:
    print(i)
    i +=1

assert i == 5
#browser = webdriver.Chrome()
#browser.get("http://suninjuly.github.io/simple_form_find_task.html")
#button = browser.find_element(By.ID, "submit_button")
