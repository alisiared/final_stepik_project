from selenium.webdriver.common.by import By

   
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    C_PASSWORD = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    REGISTER_BUTTON = (By.NAME, "registration_submit")
    
class ProductPageLocators():
    BASKET_BUTTON = (By.XPATH, '//button[@class = "btn btn-lg btn-primary btn-add-to-basket"]')
    BASKET_ALERTINNER_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    BASKET_ALERTINNER_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_SEE_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')
    BASKET_SEE_EMPTY = (By.CSS_SELECTOR, '.content_inner p')
