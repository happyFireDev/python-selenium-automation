from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify Sign In form opened')
def verify_sign_in(context):
    expected_text = 'Sign into your Target account'
    actual = context.driver.find_element(By.XPATH, "//h1[span='Sign into your Target account']").text
    assert expected_text in actual, f'Error. Text {expected_text} not in {actual}'