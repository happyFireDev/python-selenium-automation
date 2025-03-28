from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from pages.base_page import Page
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.side_nav_menu import SideNavMenu


SEARCH_RESULTS_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

SEARCH_PRODUCT_LISTING_BOX = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
SEARCH_PRODUCT_TITLE= (By.CSS_SELECTOR, "[data-test='product-title']")
SEARCH_PRODUCT_IMG = (By.CSS_SELECTOR, "img")


@when('Click Add to Cart button')
def click_add_to_cart_for_first_product(context):
    context.app.search_results_page.click_add_to_cart_for_first_product()

@when('Store product name')
def store_product_name(context):
    context.app.side_nav_menu.store_product_name(context)


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
    context.app.search_results_page.verify_search_results_text(expected_text)


@then('Verify {expected_text} in URL')
def verify_text_in_url_search_results(context, expected_text):
    context.app.base_page.verify_partial_url(expected_text)
