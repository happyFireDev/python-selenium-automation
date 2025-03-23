from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):

    CART_EMPTY_MSG = (By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")

    def open_cart_page(self):
        self.open_url('https://www.target.com/cart')


    def verify_cart_empty_message(self):
        expected_result = 'Your cart is empty'
        actual_result = self.find_element(*self.CART_EMPTY_MSG).text
        assert expected_result == actual_result, \
            f'Expected {expected_result} did not match actual {actual_result}'