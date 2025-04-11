from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from pages.base_page import Page


CLICK_T_AND_C_LINK = (By.XPATH, "//a[contains(text(), 'Target terms and conditions')]")
ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="authAlertDisplay"]')
T_AND_C_SLUG = 'terms-conditions'
LOGGED_IN_USER_ACCOUNT_SLUG = 'account?lnk=acct_nav_my_account'
SIGN_IN_TITLE_TEXT = (By.XPATH, "//h1[span='Sign into your Target account']")
SIGN_IN_TITLE_TEXT_OR_CREATE_ACCOUNT = (By.XPATH, "//h1['Sign in or create account']")
SIGN_IN_USERNAME_FIELD = (By.ID, 'username')
SIGN_IN_PASSWORD_FIELD = (By.ID, 'password')
SIGN_IN_BTN = (By.ID, 'login')



@given('Open target user account page')
def open_target_user_account_page(context):
    context.app.sign_in_page.open_url(LOGGED_IN_USER_ACCOUNT_SLUG)


@given('Store signin page from original window')
def store_original_signin_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window: ', context.original_window)


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions_link(context):
    context.app.sign_in_page.click_target_terms_and_conditions_link(CLICK_T_AND_C_LINK)


@when('Switch to terms new window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_signin_pg_windows()


@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page_is_opened(context):
    print(f'Verifying Terms and Conditions page is opened: {T_AND_C_SLUG}')
    context.app.sign_in_page.verify_terms_and_conditions_page_is_opened(T_AND_C_SLUG)


@then('Verify user is signed by url')
def verify_target_user_account_page(context):
    context.app.sign_in_page.verify_cart_page_is_opened()


@then('Verify Sign In form opened')
def verify_sign_in_title_text(context, *locator):
    expected_text = 'Sign in or create account'
    context.app.base_page.verify_text(expected_text, *SIGN_IN_TITLE_TEXT_OR_CREATE_ACCOUNT)

@then('Verify error message is shown from incorrect pw')
def verify_error_message_is_shown_from_incorrect_pw(context):
    expected_error_mgs_text = 'That password is incorrect.'
    context.app.sign_in_page.verify_error_message_is_shown_from_incorrect_pw(expected_error_mgs_text, *ERROR_MESSAGE)


@then('Input email and password on SignIn page')
def input_email_and_password(context, *locators):
    email_address = 'lirix21883@naobk.com'
    password = 'ja;oiweur5vvpq8t93u' # real password


    context.app.sign_in_page.input_email_on_sign_in(email_address,*SIGN_IN_USERNAME_FIELD)
    context.app.sign_in_page.input_password_on_sign_in(password, *SIGN_IN_PASSWORD_FIELD)

@then('Input email on SignIn page')
def input_email_and_password(context, *locators):
    email_address = '' # dummy account


    context.app.sign_in_page.input_email_on_sign_in(email_address,*SIGN_IN_USERNAME_FIELD)


@then('Input correct password on SignIn page')
def input_email_and_password(context, *locators):
    password = ''  # real password


    context.app.sign_in_page.input_password_on_sign_in(password, *SIGN_IN_PASSWORD_FIELD)


@then('Input incorrect password on SignIn page')
def input_email(context, *locators):
    password = 'ur5vvpq8t93u'  # wrong password

    context.app.sign_in_page.input_password_on_sign_in(password, *SIGN_IN_PASSWORD_FIELD)

@then('Click sign in btn on sign in')
def click_sign_in_btn_on_sign_in(context):
    context.app.base_page.wait_until_clickable(*SIGN_IN_BTN)
    context.app.sign_in_page.click_sign_in_btn_on_sign_in(*SIGN_IN_BTN)


@then('Close terms and conditions window')
def close_terms_and_conditions_window_return_to_original_to_window(context):
    context.app.sign_in_page.close_terms_and_conditions_window()


@then('Switch back to signin original window')
def return_to_original_sing_in_window(context):
    context.app.sign_in_page.return_to_original_sing_in_window(context)

