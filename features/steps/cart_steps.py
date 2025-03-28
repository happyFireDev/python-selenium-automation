from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from pages.base_page import Page




@given('Open target shopping cart page')
def open_target_main(context):
    context.app.cart_page.open_cart_page()


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty_message()


@then('Verify cart has {item_number} product(s)')
def verify_cart_items(context, item_number):
    context.app.cart_page.verify_cart_item_number(item_number)


@then('Verify cart has correct product')
def verify_cart_has_correct_product(context, *product_name):
    product_name = context.product_name  # access the stored value
    context.app.cart_page.verify_cart_has_correct_product(product_name)


@then('Verify cart page opens')
def verify_cart_page_opens(context):
    context.app.cart_page.verify_cart_page_opens()