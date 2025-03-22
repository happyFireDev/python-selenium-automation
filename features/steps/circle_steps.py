from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CELL_IDENTIFIERS = (By.CLASS_NAME, "cell-item-content")


@given('Open target circle page')
def open_target_circle_main(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {link_amount} or more links are displaying')
def verify_all_header_links_shown(context, link_amount):
    link_amount = int(link_amount)
    links = context.driver.find_elements(*CELL_IDENTIFIERS)
    assert len(links) >= link_amount, f'Expected {link_amount} links, but got {len(links)}'