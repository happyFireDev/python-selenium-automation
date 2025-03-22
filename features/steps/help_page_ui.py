from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


TITLE_TEXT = (By.CSS_SELECTOR, ".custom-h2")
SEARCH_BAR = (By.CSS_SELECTOR, ".search-input")
SEARCH_BAR_BTN = (By.CSS_SELECTOR, ".search-input")
HELP_BOXES_GRID = (By.CSS_SELECTOR, ".col-lg-12 .box-column")
MANAGE_MY_GIRD_BOXES = (By.CSS_SELECTOR, ".col-lg-12 .salesforceBox")
LOWER_GRID_BOXES =  (By.CSS_SELECTOR, ".col-lg-12 .boxSmallr")
HELP_PAGE_TEXT_TITLE = (By.CSS_SELECTOR, ".col-lg-12 .boxSmallr")


@given('Open target help page')
def open_target_main(context):
    context.driver.get('https://help.target.com/help')


@then('Verify title tile is present')
def verify_title_tile(context):
    context.driver.find_element(*TITLE_TEXT)


@then('Verify search bar is present')
def verify_search_bar(context):
    context.driver.find_element(*SEARCH_BAR)


@then('Verify search bar button is present')
def verify_search_bar_button(context):
    context.driver.find_element(*SEARCH_BAR_BTN)


@then('Verify help boxes is present')
def verify_help_boxes(context):
    help_box = context.driver.find_element(*HELP_BOXES_GRID)


@then('Verify manage my grid boxes are present')
def verify_manage_my_grid_boxes(context):
    help_box = context.driver.find_element(*MANAGE_MY_GIRD_BOXES)


@then('Verify {item_number} lower grid boxes are present')
def verify_lower_grid_boxes(context, item_number):
    grid_box_number= int(item_number)
    grid_boxes = context.driver.find_elements(*LOWER_GRID_BOXES)
    # print(f"grid_box_number = {grid_box_number}")
    # print(f"grid_boxes = {len(grid_boxes)}")
    assert len(grid_boxes) == grid_box_number, f'Expect {item_number} to have {len(grid_boxes)} boxes but received grid_box_number'

@then("Verify browse all Help pages text title are present")
def verify_browse_all_help_pages_text_title(context):
    context.driver.find_element(*HELP_PAGE_TEXT_TITLE)