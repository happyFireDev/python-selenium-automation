from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from pages.base_page import Page


class HelpPage(Page):
    # HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    # HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    TOPIC_SELECTION_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")


    # Dynamic locator => generates locator during the test
    def get_header_locator(self, header):
        # HEADER (By.XPATH, "//h1[text()=' {SUBSTRING}']") => (By.XPATH, "//h1[text()=' {SUBSTRING}']")
        return [self.HEADER[0], self.HEADER[1].replace('{SUBSTRING}', header)]

    def open_help_returns(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')


    def verify_correct_help_page_opened(self, header):
        # header = Returns / Current promotions / ...
        locator = self.get_header_locator(header)
        print(locator)
        self.wait_until_visible(*locator)


    def select_topic(self, option_value):
        dd = self.find_element(*self.TOPIC_SELECTION_DD)

        select = Select(dd)
        select.select_by_value(option_value)

    # def verify_promotions_opened(self):
    #     self.wait_until_visible(*self.HEADER_PROMOTIONS)


    # def verify_help_returns_opened(self):
    #     self.wait_until_visible(*self.HEADER_RETURNS)