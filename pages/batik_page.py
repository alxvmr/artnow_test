from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BatikPage:
    """
    A class to work with Batik
    """
    def __init__ (self, driver):
        self.driver = driver
        self.first_artwork = (By.XPATH, "//div[@id='sa_container']//div[@class='post'][1]")
        self.go_favorites = (By.XPATH, "//img[@alt='Избранное']")
        self.favorites = (By.XPATH, "//div[@id='sa_container']//div[@class='post']")
    
    def get_first(self):
        """
        Get the first element
        """
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_artwork))

    def get_header (self, elem):
        """
        Get the header
        """
        return elem.find_element(By.XPATH, ".//div[@class='ssize']").text

    def add_elem_to_favorite (self, elem):
        """
        Add item to favorites
        """
        elem.find_element(By.XPATH, ".//div[@class='heart']").click()

    def get_favorites (self):
        """
        Get favorite items
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.go_favorites)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.favorites)
        )

        favs = self.driver.find_elements (*self.favorites)
        return favs
