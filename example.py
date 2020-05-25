from selenium import webdriver
from selenium.webdriver.common.by import By


class Helper:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_id(self, element):
        return self.driver.find_element(By.ID(element))
