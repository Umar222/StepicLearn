from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "#submit_button")
    button.click()

finally:
    time.sleep(15)
    driver.quit()
