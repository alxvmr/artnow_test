from pages.main_page import MainPage
from utils.driver import get_driver

def test_search (browser):
    driver = get_driver(browser)
    main_page = MainPage(driver)

    try:
        search_word = "Жираф"

        driver.get("https://artnow.ru/")
        main_page.search (search_word)

        first_elem = main_page.get_first_elem()
        first_elem_header = main_page.get_header (first_elem)

        assert search_word in first_elem_header

    except Exception as e:
        print (f"Header: {first_elem_header}")
        # сохранить скриншот
        raise e

    finally:
        driver.quit()