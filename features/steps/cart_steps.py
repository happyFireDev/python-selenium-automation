from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
SIGN_IN_BTN = (By.XPATH, "//span[contains(text(), 'Sign in')]")
SIGN_IN_BTN_RIGHT_NAV = (By.XPATH, "//button[@data-test='accountNav-signIn']")


@given('Open target shopping cart page')
def open_target_main(context):
    context.driver.get('https://www.target.com/cart')


@when('Click on sign-in button')
def click_sign_in_button(context):
    context.driver.find_element(*SIGN_IN_BTN).click()


@when('Click on sign-in for right side navigation menu')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_BTN_RIGHT_NAV).click()
    sleep(1)


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(*CART_EMPTY_MSG).text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'


@then('Verify cart has {item_number} product(s)')
def verify_cart_items(context, item_number):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{item_number} item' in cart_summary, f"Expected {item_number} items but got {cart_summary}"