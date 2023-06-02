from .pages.product_page import ProductPage
import pytest
from .pages.basket_page import BasketPage
import time
from .pages.login_page import LoginPage

product_link_base = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# links = [f"{product_link_base}/?promo=offer{number}" for number in range(10)]
links = [pytest.param(f"{product_link_base}/?promo=offer{number}",
                      marks=pytest.mark.xfail(reason="плохой номер")) for number in range(10)]


# @pytest.mark.xfail(reason="плохой номер")
@pytest.mark.parametrize('url', links)
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.guest_add_product_to_basket()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_should_not_be_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url, 0)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.xfail(reason="fixing this bug right now")
def test_success_message_is_disappeared(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url, 0)
    page.open()
    page.success_message_is_disappeared()
    
@pytest.mark.xfail(reason="fixing this bug right now")
def test_success_message_is_not_presented(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, url, 0)
    page.open()
    page.success_message_is_not_presented()
    
          
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        page_email = str(time.time()) + "@fakemail.org"
        page_password = str(time.time()) + "abc"
        page_c_password = str(page_password)
        login_page.register_new_user(email=page_email, password=page_password, c_password=page_c_password)
        time.sleep(10)
        login_page.should_be_authorized_user()
     
    def test_user_can_add_product_to_basket(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        page.open()
        page.guest_can_add_product_to_basket()
        
    def test_user_success_message_is_not_presented(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, url)
        page.open()
        page.success_message_is_not_presented()
        
