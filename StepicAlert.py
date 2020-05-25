from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from stepicproject.stepicproject.example import Helper
import math
from data.path import Path


class Test:
    def __init__(self, driver):
        self.driver = driver

    def test_example(self):
        driver = self.driver
        wait = Helper(driver)
        driver = wait.find_element_by_id(Path.path_batton)



link = "http://suninjuly.github.io/alert_accept.html"
diver = webdriver.Chrome()

try:
    diver.get(link)
    button = diver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
    alert = diver.switch_to.alert
    alert.accept()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    number = diver.find_element(By.ID, "input_value")
    x = number.text
    y = calc(x)
    field = diver.find_element(By.ID, "answer")
    field.send_keys(y)
    send = diver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
    #alert2 = diver.switch_to.alert
    #alert2.accept()
finally:
    time.sleep(3)
    #diver.quit()