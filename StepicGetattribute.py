from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

driver = webdriver.Chrome()
driver.get(link)

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    sunduck = driver.find_element(By.ID, "treasure")
    x = sunduck.get_attribute("valuex")
    y = calc(x)
    field = driver.find_element(By.ID, "answer")
    field.send_keys(y)
    checkbox = driver.find_element(By.ID, "robotCheckbox").click()
    radiobutton = driver.find_element(By.ID, "robotsRule").click()
    button = driver.find_element(By.TAG_NAME, "[type = 'submit']").click()

finally:
    time.sleep(5)
    driver.quit()