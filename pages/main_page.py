from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MainPage:
    """
    Class for working with the main page
    """
    def __init__ (self, driver):
        self.driver = driver
        self.embroidery_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Вышитые картины']]")
        self.batik_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Батик']]")
        self.jewerly_link = (By.XPATH, "//div[@class='main_menu']//li[a[text()=' Ювелирное искусство']]")
        self.search_input = (By.XPATH, "//span[@class='search-bar']//input[@name='qs']")
        self.show_all = (By.XPATH, "//li//span[text()='Показать еще...']") 
        self.first_elem = (By.XPATH, "//div[@id='sa_container']//div[@class='post'][1]")
        self.basket_button = (By.XPATH, "//div[@id='sa_container']//div[@class='post'][1]//div[@class='oclick']")
        self.id = (By.XPATH, ".//div[@class='heart']")
        self.price = (By.XPATH, ".//div[@class='price']")

    def go_to_embroidery (self):
        """
        Go to the embroidery section
        """
        try:
            self.driver.find_element (*self.show_all).click()  
        except:
            pass

        self.driver.find_element (*self.embroidery_link).click()

    def go_to_batik (self):
        """
        Go to batik
        """
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.show_all)).click()  
        except:
            pass
        
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.batik_link)).click()

    def go_to_jewerly (self):
        """
        Jump to Jewelry Art
        """
        try:
            self.driver.find_element (*self.show_all).click()  
        except:
            pass

        self.driver.find_element (*self.jewerly_link).click()

    def search (self, query):
        """
        Search the site
        """
        try:
            self.driver.find_element (*self.show_all).click()  
        except:
            pass

        self.driver.find_element (*self.search_input).send_keys (query + Keys.RETURN)

    def get_first_elem (self):
        """
        Get the first element
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_elem))
    
    def get_header (self, elem):
        """
        Get header
        """
        return elem.find_element(By.XPATH, ".//div[@class='ssize']").text

    def get_artwork_id (self, elem):
        """
        Get product id
        """
        return elem.find_element(*self.id).get_attribute("data-id")
    
    def get_price (self, elem):
        """
        Get price
        """
        return elem.find_element(*self.price).text

if __name__ == "__main__":
    driver = webdriver.Chrome()
    main_page = MainPage (driver)
    driver.get("https://artnow.ru/")
    time.sleep(3)

    main_page.go_to_embroidery()

    driver.quit()