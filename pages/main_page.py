from selenium.webdriver.common.by import By
from pages.base_page import Page

class MainPage(Page):

    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def open_main_page(self):
        self.open_url('https://www.target.com/')

    def click_shopping_cart_icon(self):
        self.find_element(*self.CART_ICON).click()

