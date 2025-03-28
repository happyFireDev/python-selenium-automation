from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page

SIGN_IN_TITLE_TEXT = (By.XPATH, "//h1[span='Sign into your Target account']")
SIGN_IN_USERNAME_FIELD = (By.ID, 'username')
SIGN_IN_PASSWORD_FIELD = (By.ID, 'password')
SIGN_IN_BTN = (By.ID, 'login')


@then('Open target user account page')
def open_target_user_account_page(context):
    context.app.sign_in_page.open_target_user_account_page()


@then('Verify user is signed by url')
def verify_target_user_account_page(context):
    context.app.sign_in_page.verify_cart_page_is_opened()

@then('Verify Sign In form opened')
def verify_sign_in_title_text(context, *locators):
    expected_text = 'Sign into your Target account'
    context.app.base_page.verify_text(expected_text, *SIGN_IN_TITLE_TEXT)

@then('Input email and password on SignIn page')
def input_email_and_password(context, *locators):
    email_address = 'tec4196@aeshopkj.com'
    password = 'ja;oiweur5vvpq8t93u'

    context.app.sign_in_page.input_email_on_sign_in(email_address,*SIGN_IN_USERNAME_FIELD)
    context.app.sign_in_page.input_password_on_sign_in(password, *SIGN_IN_PASSWORD_FIELD)


@then('Click sign in btn on sign in')
def click_sign_in_btn_on_sign_in(context):
    context.app.sign_in_page.click_sign_in_btn_on_sign_in(*SIGN_IN_BTN)


# @then('Verify user is signed by title text')
# def Verify_user_is_signed_title_text(context, *locators):
#     context.app.base_page.verify_text(*SIGN_IN_TITLE_TEXT)