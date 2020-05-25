from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

driver = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"

driver.get(link)

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    number = driver.find_element(By.ID, "input_value")
    x = number.text
    y = calc(x)
    field = driver.find_element(By.ID, "answer")
    field.send_keys(y)
    checkbox = driver.find_element(By.ID, "robotCheckbox").click()
    button = driver.find_element(By.TAG_NAME, "[type = 'submit']")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    radiobutton = driver.find_element(By.ID, "robotsRule").click()

    button.click()
finally:
    time.sleep(5)
    driver.quit()