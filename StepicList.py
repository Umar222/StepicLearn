from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

driver = webdriver.Chrome()
driver.get(link)
try:
    x = driver.find_element(By.ID, "num1")
    num1 = x.text
    y = driver.find_element(By.ID, "num2")
    num2 = y.text
    z = str(int(num1) + int(num2))
    print(z)
    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    button = driver.find_element(By.TAG_NAME, "[type ='submit']").click()
finally:
    time.sleep(6)
    driver.quit()



