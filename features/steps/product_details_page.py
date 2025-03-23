from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, given, then
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

PRODUCT_TITLE = (By.ID, 'pdp-product-title-id')
MULTI_PRODUCT_COLOR_OPTIONS_CONTAINER = (
By.CSS_SELECTOR, "div[data-test='@web/VariationComponent'] a[class*='variantImage']")
MULTI_PRODUCT_COLOR_OPTIONS_TEXT = (By.XPATH, "//div[@data-test='@web/VariationComponent']//div[contains(@class, 'headerWrapper') and contains(., 'color')]")

# MULTI_PRODUCT_COLOR_OPTIONS_TEXT = (By.XPATH, "//div[@data-test='@web/VariationComponent']//div[contains(@class, 'headerWrapper') and contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'color')]")


@given('Open multi-option product page on target for {product_slug}')
def open_multi_option_product_page(context, product_slug):
    context.driver.get(f'https://www.target.com/p/{product_slug}')


@when('Product name')
def product_name(context):
  context.driver.wait.until(EC.presence_of_element_located(PRODUCT_TITLE),
                            message=f'Expected {PRODUCT_TITLE} to be present in the cart section')

  context.multi_option_product_title_name = context.driver.find_element(*PRODUCT_TITLE).text
  print('Multi-option product title name stored:', context.multi_option_product_title_name)


@then('Verify user can click through colors')
def verify_user_should_click_through_colors(context):

    # context.driver.wait.until(EC.text_to_be_present_in_element(
    #   MULTI_PRODUCT_COLOR_OPTIONS_TEXT, 'color'))

    color_swatches = context.driver.find_elements(
        *MULTI_PRODUCT_COLOR_OPTIONS_CONTAINER)

    for swatch in color_swatches:

        # context.driver.wait.until(EC.text_to_be_present_in_element(MULTI_PRODUCT_COLOR_OPTIONS_TEXT, 'color'))

        # Wait for color text to include 'color' (case insensitive)
        WebDriverWait(context.driver, 10).until(
          lambda driver: 'color' in driver.find_element(*MULTI_PRODUCT_COLOR_OPTIONS_TEXT).text.lower()
        )

        # Scroll to the swatch so it's visible
        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", swatch)

        # Click on the swatch to select the color
        swatch.click()

        color_name_element = context.driver.find_element(
            *MULTI_PRODUCT_COLOR_OPTIONS_TEXT)

        color_name = color_name_element.text.strip()

        # Print the color name to the console
        print(f"Selected color: {color_name}")

        # Make sure the color name isn't empty
        assert color_name, "No color name found after clicking swatch."
