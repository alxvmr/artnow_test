from pages.main_page import MainPage
from pages.batik_page import BatikPage
from utils.driver import get_driver
from utils import allure

def test_batik_favs (browser):
    """
    Go to “Батик”, add the first painting to favorites, check,
    that the selected painting is saved in the “Избранное” section. 
    """
    driver = get_driver(browser)
    main_page = MainPage(driver)
    batik_page = BatikPage(driver)

    try:
        driver.get("https://artnow.ru/")
        main_page.go_to_batik()
        first_elem = batik_page.get_first()
        first_elem_header = batik_page.get_header (first_elem)
        batik_page.add_elem_to_favorite(first_elem)
        favs = batik_page.get_favorites()

        is_here = False
        for f in favs:
            if first_elem_header == batik_page.get_header (f):
                is_here = True
                break
        assert is_here, "Item not in favorites"

    except Exception as e:
        allure.take_screenshot (driver, "Favorite picture")
        raise e

    finally:
        driver.quit()