from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):


    CART_EMPTY_MSG = (By.CSS_SELECTOR,"[data-test='boxEmptyMsg']")
    CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
    CART_PRODUCT_TITLE_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


    def open_cart_page(self):
        self.open_url(f'{self.base_url}cart')


    def verify_cart_page_opens(self):
        self.verify_url(f'{self.base_url}cart')


    def verify_cart_empty_message(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)


    def verify_cart_item_number(self, item_number):
        print(f'(no unpacking) Cart summery details: ', self.CART_SUMMARY)
        print(f'(with unpacking) Cart summery details: ', *self.CART_SUMMARY)

        self.verify_partial_text(f'{item_number}', *self.CART_SUMMARY)


    def verify_cart_has_correct_product(self, product_name):
        self.wait_until_visible(*self.CART_PRODUCT_TITLE_NAME)

        self.verify_partial_text(f'{product_name}' , *self.CART_PRODUCT_TITLE_NAME)

        # product_name_in_cart = self.find_element(*self.CART_PRODUCT_TITLE_NAME).text
        #
        # assert product_name[:10] == product_name_in_cart[:10], \
        #     f"Expected {product_name[:10]} did not match {product_name_in_cart[:10]}"