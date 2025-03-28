from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CIRCLE_BENEFITS_CELLS = (By.CSS_SELECTOR, ".cell-item-content")

@given("Open target circle page")
def open_target_circle_page(context):
    context.driver.get('https://www.target.com/circle ')

@when("Page loads Then Verify cells are present")
def verify_cells_present(context):
    context.driver.find_elements(*CIRCLE_BENEFITS_CELLS)

@then('Verify {link_amount} or more links are displaying')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*CELL_IDENTIFIERS)
    assert len(links) >= link_amount, f'Expected {link_amount} links, but got {len(links)}'