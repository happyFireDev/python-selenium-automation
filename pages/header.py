from selenium.webdriver.common.by import By
from pages.base_page import Page

class Header(Page):

    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search(self, text):
        print(f"Searching for: {text}")
        self.input_text(text, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)





