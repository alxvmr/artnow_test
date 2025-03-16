from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmbroideryPage:
    def __init__ (self, driver):
        self.driver = driver
        self.genre_filter = (By.XPATH, "//label[contains(text(), 'Городской пейзаж')]")
        self.apply_button = (By.XPATH, "//div[@class='seform']//button[text()='Применить']")
        self.artwork_list = (By.XPATH, "//div[@id='sa_container']")

    def select_genre_filter (self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.genre_filter)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apply_button)).click()

    def is_artwork_present (self, artwork_name):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.artwork_list))
        return artwork_name in self.driver.find_element(*self.artwork_list).text