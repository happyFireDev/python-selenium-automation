from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
FIRST_PRODUCT = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'


@then('Click on first product on search results page')
def click_first_product(context):
    sleep(4)
    product_string = context.driver.find_element(*FIRST_PRODUCT).click()
    print(product_string)


@then('Click add to cart in side-menu pop-up')
def click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(5)
