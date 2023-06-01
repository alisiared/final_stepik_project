from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, '//button[@class = "btn btn-lg btn-primary btn-add-to-basket"]')
    BASKET_ALERTINNER_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_ALERTINNER_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
