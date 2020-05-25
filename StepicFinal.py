import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class StepicFinal(unittest.TestCase):

    def test_abs1(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://suninjuly.github.io/registration1.html")
        self.driver.find_element(By.XPATH, "//div[1]/div[1]/input").send_keys("Мой ответ")
        self.driver.find_element(By.XPATH, "//div[1]/div[2]/input").send_keys("Мой ответ")
        self.driver.find_element(By.XPATH, "//div[1]/div[3]/input").send_keys("Мой ответ")
        self.driver.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = self.driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_abs2(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://suninjuly.github.io/registration2.html")
        self.driver.find_element(By.XPATH, "//div[1]/div[1]/input").send_keys("Мой ответ")
        self.driver.find_element(By.XPATH, "//div[1]/div[2]/input").send_keys("Мой ответ")
        self.driver.find_element(By.XPATH, "//div[1]/div[3]/input").send_keys("Мой ответ")
        self.driver.find_element_by_css_selector("button.btn").click()
        time.sleep(1)
        welcome_text_elt = self.driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()
