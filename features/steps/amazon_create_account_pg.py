from selenium.webdriver.common.by import By
from behave import given, when, then
from time import time

@given('Open Amazon creation account page')
def open_target_main(context):
    context.driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=64NBPX3SCT41VWJP4415&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


@when('Enter valid data into the name and email fields')
def enter_valid_data(context):
    name_field = context.driver.find_element(By.ID, "ap_customer_name")
    email_field = context.driver.find_element(By.ID, "ap_email")
    name_field.send_keys("Sam Hill")
    email_field.send_keys("sam.hill@example.com")


@then('Verify using amazon create page')
def verify_create_account_page(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")


@then('Check Amazon logo')
def amazon_logo(context):
    context.driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']") # //tag[@attr='value']


@then('Check name field')
def check_name_field(context):
    context.driver.find_element(By.ID, "ap_customer_name") # //tag[@attr='value']


@then('Check email field')
def check_email_field(context):
    context.driver.find_element(By.ID, "ap_email") # //tag[@attr='value']


@then('Password field')
def password_field(context):
    context.driver.find_element(By.ID, "ap_password")


@then('Password field check')
def password_field_check(context):
    context.driver.find_element(By.ID, "ap_password_check")


@then('Continue button')
def continue_button(context):
    context.driver.find_element(By.ID, "continue")


@then('Conditions of use link')
def conditions_of_use(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")


@then('Privacy notice link')
def private_notice_link(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")


@then('Sign-In link')
def sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")
