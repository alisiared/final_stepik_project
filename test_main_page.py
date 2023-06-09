from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    
    def test_guest_should_see_login_link(self, browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, url)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        url = "http://selenium1py.pythonanywhere.com/"
        page = BasketPage(browser, url)
        page.open()
        page.guest_cant_see_product_in_basket_opened_from_main_page()
