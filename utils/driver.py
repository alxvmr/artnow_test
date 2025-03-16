from selenium import webdriver

def get_driver (browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError ("Unsupported browser")
    
    driver.implicitly_wait (10)
    return driver