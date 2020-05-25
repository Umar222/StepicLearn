from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
driver.get(link)
try:
    button = WebDriverWait(driver, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
    rule = driver.find_element(By.ID, "book").click()

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    number = driver.find_element(By.ID, "input_value")
    x = number.text
    y = calc(x)
    driver.execute_script("window.scrollBy(0, 10);")
    field = driver.find_element(By.ID, "answer")
    field.send_keys(y)
    submit = driver.find_element(By.ID, "solve").click()
    ok = driver.switch_to.alert
    ok.accept()
    are = driver.find_element_by_class_name()
finally:
    time.sleep(1)
    driver.quit()






