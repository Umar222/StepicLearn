from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"


try:
    driver = webdriver.Chrome()
    driver.get(link)
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")
    button = driver.find_element(By.CSS_SELECTOR, "form>button")
    button.click()

finally:
    time.sleep(5)
    driver.quit()



