from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then



CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
CART_PRODUCT_TITLE_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
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
    context.driver.wait.until(EC.visibility_of_element_located(SIGN_IN_BTN_RIGHT_NAV))
    context.driver.find_element(*SIGN_IN_BTN_RIGHT_NAV).click()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(*CART_EMPTY_MSG).text
    assert expected_result == actual_result, \
        f'Expected {expected_result} did not match actual {actual_result}'


@then('Verify cart has {item_number} product(s)')
def verify_cart_items(context, item_number):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert f'{item_number} item' in cart_summary, \
        f"Expected {item_number} items but got {cart_summary}"

@then('Verify cart has correct product')
def verify_cart_item_are_correct(context):
    # context.product_name ==> name of the product
    context.driver.wait.until(EC.visibility_of_element_located(CART_PRODUCT_TITLE_NAME), message = f'Error - could not find product in the cart title section: {CART_PRODUCT_TITLE_NAME}')

    product_name_in_cart = context.driver.find_element(*CART_PRODUCT_TITLE_NAME).text
    assert context.product_name[:10] == product_name_in_cart[:10], \
        f"Expected {context.product_name[:10]} did not match {product_name_in_cart[:10]}"