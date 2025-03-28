from pages.base_page import Page

class SignInPage(Page):

    LOGGED_IN_USER_ACCOUNT_SLUG = 'account?lnk=acct_nav_my_account'

    def open_target_user_account_page(self):
        self.open_url(f'{self.base_url}{self.LOGGED_IN_USER_ACCOUNT_SLUG}')

    def verify_cart_page_is_opened(self):
        self.verify_url(f'{self.base_url}{self.LOGGED_IN_USER_ACCOUNT_SLUG}')

    def verify_sign_in_title_text(self, expected_text):
        self.verify_text(expected_text)


    def input_email_on_sign_in(self, email, *locator):
        self.input_text(email, *locator)


    def input_password_on_sign_in(self, password, *locator):
        self.input_text(password, *locator)


    def click_sign_in_btn_on_sign_in(self, *locator):
        self.click(*locator)

    # def Verify_user_is_signed_title_text(self):
    #     self.verify_text('Sign In')