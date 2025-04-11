from selenium.webdriver.common.by import By
from selenium.common import ElementClickInterceptedException, StaleElementReferenceException
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):

    ADD_TO_CART_FIRST_PRODUCT = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    FAVORITES_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TEXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def verify_search_results_text(self, expected_text):
        self.verify_partial_text(expected_text, *self.SEARCH_RESULTS_TEXT)

    def verify_text_in_search_results(self, expected_partial_url):
        self.verify_partial_url(expected_partial_url, *self.SEARCH_RESULTS_TEXT)

    def verify_full_url_results(self, expected_full_url):
        self.verify_partial_url(expected_full_url, *self.SEARCH_RESULTS_TEXT)

    def click_add_to_cart_for_first_product(self):
        try:
            print(f"[DEBUG] Using locator: {self.ADD_TO_CART_FIRST_PRODUCT}")

            self.wait_until_clickable(*self.ADD_TO_CART_FIRST_PRODUCT)

            element = self.find_element(*self.ADD_TO_CART_FIRST_PRODUCT)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            element.click()

        except StaleElementReferenceException:
            print("[WARN] StaleElementReferenceException caught. Retrying...")

            print(f"[DEBUG] Using locator: {self.ADD_TO_CART_FIRST_PRODUCT}")

            element = self.find_element(*self.ADD_TO_CART_FIRST_PRODUCT)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            element.click()

    def hover_over_favorites_icon(self):
        self.hover_over_element(*self.FAVORITES_BTN)


    def verify_fav_tooltip(self):
        self.wait_until_visible(*self.FAVORITES_TOOLTIP_TEXT)