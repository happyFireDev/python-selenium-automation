from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


#  Scenario: Testing is the user cart is e


@when('Click on shopping cart icon')
def click_shopping_icon(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()


@then('Verify cart is empty')
def verify_cart_results_is_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


##   Scenario: verify that a logged out user can navigate to Sign In

@when('Click on sign-in button')
def click_sign_in_button(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]").click()

@when('Click on sign-in for right side navigation menu')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(1)

@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//h1[span='Sign into your Target account']").text
    assert expected_text in actual, f'Error. Text {expected_text} not in {actual}'
