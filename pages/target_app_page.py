from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetAppPage(Page):
    PP_LINK = (By.XPATH, "//a[text()='Privacy policy']")

    def open_target_app(self):
        self.open_url('https://www.target.com/c/target-app/')

    def click_pp_link(self):
        self.click(*self.PP_LINK)

    def verify_pp_opened(self):
        self.verify_partial_url('target-privacy-policy')

    def close_pp_current_active_page(self):
        self.close()

    def switch_back_to_main_app_window(self, context):
        self.switch_to_window_by_id(context.original_window)
