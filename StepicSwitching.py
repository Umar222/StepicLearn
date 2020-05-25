from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

driver = webdriver.Chrome()
try:
    driver.get(link)
    button = driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    first_window = driver.window_handles[0]

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    number = driver.find_element(By.ID, "input_value")
    x = number.text
    y = calc(x)
    field = driver.find_element(By.ID, "answer")
    field.send_keys(y)
    submit = driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
finally:
    time.sleep(10)
    driver.quit()