from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
# Ваш код, который заполняет обязательные поля
    first_name = driver.find_element(By.XPATH, "//div[1]/div[1]/input")
    first_name.send_keys("Мой ответ")
    second_name = driver.find_element(By.XPATH, "//div[1]/div[2]/input")
    second_name.send_keys("Мой ответ")
    field_Email = driver.find_element(By.XPATH, "//div[1]/div[3]/input")
    field_Email.send_keys("Мой ответ")
    # Отправляем заполненную форму
    button = driver.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    #driver.quit()