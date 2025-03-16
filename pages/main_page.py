from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class MainPage:
    def __init__ (self, driver):
        self.driver = driver
        self.embroidery_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Вышитые картины']]")
        self.batik_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Батик']]")
        self.jewerly_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Ювелирное искусство']]")
        self.search_input = (By.XPATH, "//span[@class='search-bar']//input[@name='qs']")
        self.show_all = (By.XPATH, "//li//span[text()='Показать еще...']")      

    def go_to_embroidery (self):
        try:
            self.driver.find_element (*self.show_all).click()  
        except:
            pass

        self.driver.find_element (*self.embroidery_link).click()

    def go_to_batik (self):
        try:
            self.driver.find_element (*self.show_all).click()  
        except:
            pass

        self.driver.find_element (*self.batik_link).click()

    def go_to_jewerly (self):
        try:
            self.driver.find_element (*self.show_all).click()  
        except:
            pass

        self.driver.find_element (*self.jewerly_link).click()

    def search (self, query):
        try:
            self.driver.find_element (*self.show_all).click()  
        except:
            pass

        self.driver.find_element (*self.search_input).send_keys (query + Keys.RETURN)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    main_page = MainPage (driver)
    driver.get("https://artnow.ru/")
    time.sleep(3)

    main_page.go_to_embroidery()

    driver.quit()