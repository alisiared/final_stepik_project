import time
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators
import math

class ProductPage(BasePage):
    def guest_add_product_to_basket(self):
        self.guest_can_add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_be_same_name()
        self.should_be_same_price()
        
    def guest_can_add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
            
    def should_be_same_name(self):
        alertinner_name = self.browser.find_element(*ProductPageLocators.BASKET_ALERTINNER_NAME)
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        assert alertinner_name.text == name.text, "Names are not equal"
        
    def should_be_same_price(self):
        alertinner_price = self.browser.find_element(*ProductPageLocators.BASKET_ALERTINNER_PRICE)
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        assert alertinner_price.text == price.text, "Price are not equal"