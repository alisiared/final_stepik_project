import time
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    
    def guest_cant_see_product_in_basket_opened_from_main_page(self):
        basket_see = self.browser.find_element(*BasketPageLocators.BASKET_SEE_BUTTON)
        basket_see.click()
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_SEE_EMPTY), "Busket is not empty, but should be"
        
    def guest_cant_see_product_in_basket_opened_from_product_page(self):
        basket_see = self.browser.find_element(*BasketPageLocators.BASKET_SEE_BUTTON)
        basket_see.click()
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_SEE_EMPTY), "Busket is not empty, but should be"




