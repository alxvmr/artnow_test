from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmbroideryPage:
    """
    Class to work with the embroidery page
    """
    def __init__ (self, driver):
        self.driver = driver
        self.genre_filter = (By.XPATH, "//label[contains(text(), 'Городской пейзаж')]")
        self.apply_button = (By.XPATH, "//div[@class='seform']//button[text()='Применить']")
        self.artwork_list = (By.XPATH, "//div[@id='sa_container']//div[@class='ssize']")
        self.style_info = (By.XPATH, "//div[@class='infocontainer']//span[text()[contains(.,'Стиль')]]//../a")

    def select_genre_filter (self):
        """
        Set embroidery filter
        """
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.genre_filter)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apply_button)).click()

    def click_artwork (self, artwork_name):
        """
        Click on an item
        """
        artwork_card = (By.XPATH, f"//div[@id='sa_container']//div[text()='{artwork_name}']")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(artwork_card)).click()

    def get_style (self):
        """
        Get the style 
        """
        style = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.style_info))
        return style.text

    def is_artwork_present (self, artwork_name):
        """
        Checking for the presence of an element
        """
        elems = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.artwork_list)).find_elements(*self.artwork_list)
        return any (artwork_name in el.text for el in elems)
