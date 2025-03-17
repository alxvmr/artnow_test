from pages.main_page import MainPage
from pages.embroidery_page import EmbroideryPage
from utils.driver import get_driver

# @pytest.mark.parametrize ("browser", ["chrome", "firefox"])
def test_issuance_presence (browser):
    driver = get_driver(browser)
    main_page = MainPage(driver)
    embroidery_page = EmbroideryPage(driver)

    try:
        driver.get("https://artnow.ru/")
        main_page.go_to_embroidery()

        embroidery_page.select_genre_filter()
        
        artwork_name = "Трамвайный путь"
        assert embroidery_page.is_artwork_present (artwork_name), f"The artwork {artwork_name} was not found in the rendition"

    except Exception as e:
        # сохранить скриншот
        raise e

    finally:
        driver.quit()

def test_realism (browser):
    driver = get_driver(browser)
    driver.get("https://artnow.ru/")

    main_page = MainPage(driver)
    embroidery_page = EmbroideryPage(driver)

    try:
        main_page.go_to_embroidery()

        embroidery_page.select_genre_filter()
        
        artwork_name = "Трамвайный путь"
        embroidery_page.click_artwork (artwork_name)
        cur_style = embroidery_page.get_style ()
        assert cur_style == "Реализм", f"The style of the artwork '{artwork_name}' does not equal 'Реализм'"

    except Exception as e:
        # сохранить скриншот
        raise e

    finally:
        driver.quit()