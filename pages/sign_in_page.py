from pages.base_page import Page

class SignInPage(Page):



    def open_target_user_account_page(self, url_slug):
        self.open_url(f'{self.base_url}{url_slug}')


    def click_target_terms_and_conditions_link(self, locator):
        print('locator', locator)
        self.wait_until_clickable_click(*locator)

    def click_sign_in_btn_on_sign_in(self, *locator):
        self.click(*locator)


    def verify_cart_page_is_opened(self):
        self.verify_url(f'{self.base_url}{self.LOGGED_IN_USER_ACCOUNT_SLUG}')


    def verify_sign_in_title_text(self, expected_text):
        self.verify_text(expected_text)


    def verify_error_message_is_shown_from_incorrect_pw(self,expected_error_mgs_text, *locator):
        self.verify_text(expected_error_mgs_text, *locator)


    def verify_terms_and_conditions_page_is_opened(self, url_slug):
        self.verify_partial_url(url_slug)


    def input_email_on_sign_in(self, email, *locator):
        self.input_text(email, *locator)


    def input_password_on_sign_in(self, password, *locator):
        self.slow_type(password, *locator)


    def switch_to_signin_pg_windows(self):
        self.switch_to_new_window()


    def store_original_signin_window(self):
        self.switch_to_new_window()


    def close_terms_and_conditions_window(self):
        self.close()


    def return_to_original_sing_in_window(self, context):
        self.switch_to_window_by_id(context.original_window)
