from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/math.html"

driver = webdriver.Chrome()

try:
    driver.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    text_field = driver.find_element(By.CLASS_NAME, "form-control")
    text_field.send_keys(x)
    checkbox = driver.find_element(By.CSS_SELECTOR, "[type = 'checkbox']")
    checkbox.click()
    radiobutton = driver.find_element(By.ID, "robotsRule")
    radiobutton.click()
    button = driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
finally:
    time.sleep(10)
    #driver.quit()




