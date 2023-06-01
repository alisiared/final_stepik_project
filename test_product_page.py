from .pages.product_page import ProductPage
import pytest

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
   
    