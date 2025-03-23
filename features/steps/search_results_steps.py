from selenium.common import ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_FIRST_PRODUCT = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4 ")
SEARCH_PRODUCT_LISTING_BOX = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
SEARCH_PRODUCT_TITLE= (By.CSS_SELECTOR, "[data-test='product-title']")
SEARCH_PRODUCT_IMG = (By.CSS_SELECTOR, "img")


@when('Click Add to Cart button')
def click_add_to_cart_for_first_product(context):
    try:
        # Wait until clickable
        context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_FIRST_PRODUCT))

        # Re-locate fresh each time before clicking
        element = context.driver.find_element(*ADD_TO_CART_FIRST_PRODUCT)

        # Scroll into view
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # Click
        element.click()

    except StaleElementReferenceException:
        # Retry once if it's stale
        element = context.driver.find_element(*ADD_TO_CART_FIRST_PRODUCT)
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()


@when('Store product name')
def store_product_name(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
                              message = 'Error - could not find product name in the cart section side navigation')

    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored:', context.product_name)


@when('Click Add to Cart in side-menu pop-up')
def click_add_to_cart(context):
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_ADD_TO_CART_BTN))
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()


@when('Verify search results have a product image and name')
def verify_search_results_name_img(context):
    # # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,1000)", "")
    sleep(2)

    products = context.driver.find_elements(*SEARCH_PRODUCT_LISTING_BOX)[:]

    for product in products:
        title_element = product.find_element(*SEARCH_PRODUCT_TITLE).text
        print(title_element)
        assert title_element, f"product title not found {title_element}"
        # Find the image inside each product
        product.find_element(*SEARCH_PRODUCT_IMG)


@then('Verify correct search results shown for {expected_text}')
def verify_search_results(context, expected_text):
    context.app.search_results_page.verify_search_results_text( expected_text)

    # actual_text = context.driver.find_element(*SEARCH_RESULTS_TEXT).text
    # assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

