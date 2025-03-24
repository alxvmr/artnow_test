from pages.main_page import MainPage
from pages.basket_page import BasketPage
from utils.driver import get_driver
from utils import allure

def test_basket (browser):
    """
    Go to “Ювелирное искусство”, add the first item to the
    cart, check that the selected item is in the cart, 
    the cost of the item has not changed.
    """
    driver = get_driver(browser)
    main_page = MainPage(driver)
    basket_page = BasketPage(driver)

    try:
        driver.get("https://artnow.ru/")
        main_page.go_to_jewerly()

        first_elem = main_page.get_first_elem()
        first_elem_id = "cart" + main_page.get_artwork_id (first_elem)
        first_elem_price = main_page.get_price (first_elem)
        basket_page.add_basket (first_elem)

        basket_page.go_to_basket()
        elems_basket = basket_page.get_all_elements()

        ch_elem = None
        for e in elems_basket:
            id = basket_page.get_id (e)
            if id == first_elem_id:
                ch_elem = e
                break
        
        assert ch_elem
        if (ch_elem):
            basket_price = basket_page.get_price(ch_elem)
            assert basket_price == first_elem_price

    except Exception as e:
        if ch_elem == None:
            print ("В корзине нет нужного элемента\n")
            allure.take_screenshot (driver, "No element")
        else:
            print (f"Стоимость товаров не совпадает: {first_elem_price} {basket_price}")
            allure.take_screenshot (driver, "Incorrect cost")
        raise e

    finally:
        driver.quit()