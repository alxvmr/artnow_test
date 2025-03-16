from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPage:
    def __init__ (self, driver):
        self.driver = driver
        self.embroidery_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Вышитые картины']]")
        self.batik_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Батик']]")
        self.jewerly_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Ювелирное искусство']]")
        self.search_input = (By.XPATH, "//span[@class='search-bar']//input[@name='qs']")

    def go_to_embroidery (self):
        self.driver.find_element (*self.embroidery_link).click()

    def go_to_batik (self):
        self.driver.find_element (*self.batik_link).click()

    def go_to_jewerly (self):
        self.driver.find_element (*self.jewerly_link).click()

    def search (self, query):
        self.driver.find_element (*self.search_input).send_keys (query + Keys.RETURN)