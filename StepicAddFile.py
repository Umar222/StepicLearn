from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import math

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()
try:
    #print(os.path.abspath(__file__))
    driver.get(link)
    field = driver.find_elements(By.TAG_NAME, "[type = 'text']")
    for element in field:
        element.send_keys("Мой ответ")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element = driver.find_element(By.ID, "file")
    element.send_keys(file_path)
    button = driver.find_element(By.TAG_NAME, "[type = 'submit']").click()
finally:
    time.sleep(5)
    driver.quit()
