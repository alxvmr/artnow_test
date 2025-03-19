from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasketPage:
    def __init__ (self, driver):
        self.driver = driver
        self.first_elem = (By.XPATH, "//div[@id='sa_container']//div[@class='post'][1]")
        self.all_elem = (By.XPATH, "//div[@id='main_container']//div[@class='c_row']")
        self.close_button = (By.XPATH, "//button[@id='close-button']")
        self.basket_button = (By.XPATH, "//span[@class='basketico']//img")
        self.price = (By.XPATH, ".//div[@class='price']")

    def get_first_elem (self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_elem))

    def add_basket (self, elem):
        basket_button = elem.find_element(By.XPATH, ".//div[@class='oclick']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(basket_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_button)).click()

    def go_to_basket (self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.basket_button)).click()

    def get_price (self, elem):
        price = elem.find_element(*self.price)
        return price.text
    
    def get_id (self, elem):
        return elem.get_attribute ("id")
    
    def get_all_elements (self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.all_elem))
        return self.driver.find_elements(*self.all_elem)